#!/usr/bin/env python3
# SPDX-License-Identifier: CC-BY-SA-4.0
# Copyright (c) 2026 ZT-DSP Suite maintainers (copyright holder: SCAL-ROAM)
"""Structural self-check for the ZT-DSP specification repository.

Nine checks. Exit code 0 only when all pass. Run from the repository root:

    python scripts/check.py
"""

import io
import os
import re
import glob
import sys

CN = "cn/spec/ZT-DSP-1.0.1-总指导.md"
EN = "en/spec/ZT-DSP-1.0.1-Master_Guide.md"

results = []


def record(name, ok, detail):
    results.append((name, ok, detail))


def read(path):
    return io.open(path, encoding="utf-8", errors="ignore").read()


# 1. Languages stay in step
cn = read(CN).splitlines()
en = read(EN).splitlines()
h1cn = [l for l in cn if l.startswith("# ")]
h1en = [l for l in en if l.startswith("# ")]
def shape(lines):
    h = sum(1 for l in lines if l.startswith("#"))
    t = sum(1 for l in lines if l.startswith("|"))
    b = sum(1 for l in lines if l.startswith(("- ", "* ")))
    n = sum(1 for l in lines if re.match(r"^\d+\. ", l))
    para, cur = 0, False
    for l in lines:
        if not l.strip() or l.startswith(("#", "|")) or l.startswith(("- ", "* ")) or re.match(r"^\d+\. ", l):
            cur = False
            continue
        if not cur:
            para += 1
            cur = True
    return h, t, b, n, para


scn, sen = shape(cn), shape(en)
record("1 language parity", scn == sen,
       "headings %d/%d, table rows %d/%d, list items %d/%d, numbered %d/%d, paragraphs %d/%d"
       % (scn[0], sen[0], scn[1], sen[1], scn[2], sen[2], scn[3], sen[3], scn[4], sen[4]))

# 2. No placeholders left behind
found = []
for dp, dn, fs in os.walk("."):
    if ".git" in dp:
        continue
    for f in fs:
        if f.endswith(".md"):
            t = read(os.path.join(dp, f))
            for kw in ("TODO", "TBD", "FIXME", "XXX", "待补"):
                if kw in t:
                    found.append("%s:%s" % (f, kw))
record("2 no placeholders", not found, "%d found" % len(found))

# 3. Every relative link resolves
broken = []
for dp, dn, fs in os.walk("."):
    if ".git" in dp:
        continue
    for f in fs:
        if not f.endswith(".md"):
            continue
        p = os.path.join(dp, f)
        for m in re.finditer(r"\]\(([^)#\s]+?)\)", read(p)):
            link = m.group(1)
            if link.startswith(("http", "mailto:", "//")):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(dp, link))):
                broken.append("%s -> %s" % (f, link))
record("3 links resolve", not broken, "%d broken" % len(broken))

# 4. No duplicate level-1 heading
dup = [h for h in set(h1en) if h1en.count(h) > 1]
record("4 unique headings", not dup, "; ".join(sorted(dup)) if dup else "all unique")

# 5. Glossary agrees with the specification text
def norm(s):
    return re.sub(r"[\s\-]+", " ", s.lower()).strip()

rows = []
for line in read("cn/术语对照表.md").splitlines():
    p = [x.strip() for x in line.strip("|").split("|")]
    if len(p) >= 2 and p[0] and not p[0].startswith("中文") and not p[0].startswith("---"):
        rows.append((p[0], p[1]))
spec_norm = norm("\n".join(en))
cn_text = "\n".join(cn)
conflicts = [(c, e) for c, e in rows
             if c in cn_text and e and len(e) > 3
             and not re.fullmatch(r"[A-Z0-9\-]+", e)
             and norm(e) not in spec_norm]
record("5 glossary agrees", not conflicts, "%d conflicts" % len(conflicts))

# 6. Licence set is complete
need = ["LICENSE", "LICENSING.md", "NOTICE", "TRADEMARK.md", "CONTRIBUTING.md", "CONTRIBUTORS.md"]
missing = [n for n in need if not os.path.exists(n)]
record("6 licence files", not missing, ("missing " + ", ".join(missing)) if missing else "6 present")

# 7. The publication record carries the patent statement, in one place
rec_txt = read("PUBLICATION-RECORD.md") if os.path.exists("PUBLICATION-RECORD.md") else ""
has_patent = "## Patents" in rec_txt
no_split = not any(os.path.exists(n) for n in ("cn/PRIOR-PUBLICATION.md", "en/PRIOR-PUBLICATION.md"))
record("7 publication record", has_patent and no_split,
       "Patents section present" if has_patent and no_split else
       ("missing ## Patents in PUBLICATION-RECORD.md" if not has_patent else "a split statement file is back"))

# 8. Every markdown file is reachable from the document map in README.md
allmd = set()
for dp, dn, fs in os.walk("."):
    if ".git" in dp:
        continue
    for f in fs:
        if f.endswith(".md"):
            allmd.add(os.path.normpath(os.path.join(dp, f)).replace("\\", "/").lstrip("./"))
readme = read("README.md")
mapped = set()
for m in re.finditer(r"\]\(([^)#\s]+?)\)", readme):
    link = m.group(1)
    if link.endswith(".md"):
        mapped.add(os.path.normpath(link).replace("\\", "/").lstrip("./"))
orphans = sorted(allmd - mapped - {"README.md"})
record("8 map covers all files", not orphans,
       ("unmapped: " + ", ".join(orphans)) if orphans else "all mapped")

# 9. Every appendix reference points at an appendix that exists
existing = set(re.findall(r"^# Appendix ([A-Z])", "\n".join(en), re.M))
refs = set()
for m in re.finditer(r"Appendix ([A-Z])\.", "\n".join(en)):
    head = "\n".join(en)[max(0, m.start() - 14):m.start()]
    if "RFC" in head:
        continue  # references an RFC appendix, not one of ours
    refs.add(m.group(1))
dangling = sorted(refs - existing)
record("9 appendix references", not dangling, ("dangling " + ", ".join(dangling)) if dangling else "all resolve")

# ---------- external links: report only ----------
# Until now every http(s) link was skipped here, so a 404 could not be seen.
# This block reports them and never fails the run: a network blip or a
# third-party outage must not turn the gate red.
ext_warn = []
try:
    import urllib.request
    pat = re.compile(r"https?://[^\s)\]]+")
    seen = set()
    for rel in sorted(glob.glob("**/*.md", recursive=True)):
        try:
            body = open(rel, encoding="utf-8").read()
        except Exception:
            continue
        for u in pat.findall(body):
            u = u.rstrip(chr(96) + chr(34) + chr(39) + ".,;:)")
            if u.endswith(".git") or u in seen:
                continue
            seen.add(u)
            if len(seen) > 40:
                break
            try:
                req = urllib.request.Request(u, method="HEAD",
                                             headers={"User-Agent": "zt-dsp-check"})
                code = urllib.request.urlopen(req, timeout=6).status
                if code >= 400:
                    ext_warn.append((u, code))
            except Exception as e:
                ext_warn.append((u, getattr(e, "code", "unreachable")))
except Exception as e:
    print("  external link check skipped: %s" % e)

if ext_warn:
    print()
    print("WARN external links (not counted in the 9):")
    for u, code in ext_warn[:10]:
        print("   %s  ->  %s" % (u, code))

for name, ok, detail in results:
    print("%s  %-24s %s" % ("PASS" if ok else "FAIL", name, detail))
failed = [r for r in results if not r[1]]
print("")
print("%d/9 passed" % (9 - len(failed)))
sys.exit(0 if not failed else 1)
