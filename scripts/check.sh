#!/usr/bin/env bash
# Repository-local self-check. Runs in the git root.
set -eu
root=$(git rev-parse --show-toplevel)
cd "$root"

cn_file="cn/spec/ZT-DSP-1.0.2-总指导.md"
en_file="en/spec/ZT-DSP-1.0.2-Master_Guide.md"
for f in "$cn_file" "$en_file"; do
  [ -f "$f" ] || { echo "missing spec file: $f"; exit 1; }
done

python - "$cn_file" "$en_file" <<'PY'
import re, sys


def shape(path):
    lines = open(path, encoding="utf-8").read().split("\n")
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
    return (h, t, b, n, para)


a, b = shape(sys.argv[1]), shape(sys.argv[2])
if a != b:
    print("spec mirrors differ in shape: cn=%s en=%s" % (a, b))
    sys.exit(1)
print("spec mirrors aligned: headings %d, table rows %d, list items %d, numbered %d, paragraphs %d" % a)
PY
