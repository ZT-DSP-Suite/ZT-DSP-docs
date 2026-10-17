# Publication Record

> Readers: anyone who needs the public disclosure date, and any examiner or auditor who needs to reproduce it.
> Status: current.

## What was published

| Item | Value |
|---|---|
| Repository | `https://github.com/ZT-DSP-Suite/ZT-DSP-docs` |
| Visibility | PUBLIC |
| Created (UTC) | 2026-10-17T17:43:46Z |
| Last pushed (UTC) | 2026-10-17T19:04:50Z (this record's own commit) |
| Default branch | `main` |
| First public commit | `3642082ee5e805428e8aa11200555c09f04f3198` |
| Release tag | `pub-2026-10-18` → `3642082` (annotated) |
| Earlier tag | `docs-v1.0.0` → `837bfb8` (annotated) |
| Branches at publication | `main` only |

## Content hashes

| File | SHA-256 |
|---|---|
| `cn/spec/ZT-DSP-1.0.1-总指导.md` | `0847e4046c6bf9e0b9b799d58709d20d4c063cf97f026f6f9e874f6eddfb26d3` |
| `en/spec/ZT-DSP-1.0.1-Master_Guide.md` | `7824bd19ccbcf29185aa1331b4c87db8a3b8ed477e38bc9cc9504d5dca1c8fd0` |

## How to reproduce

1. Read the timestamps: `gh api repos/ZT-DSP-Suite/ZT-DSP-docs --jq '{createdAt,pushedAt,visibility}'`.
2. Read the published commit: `gh api repos/ZT-DSP-Suite/ZT-DSP-docs/commits/main --jq .sha`.
3. Read the tags: `git ls-remote --tags https://github.com/ZT-DSP-Suite/ZT-DSP-docs.git`.
4. Recompute a hash: `sha256sum 'cn/spec/ZT-DSP-1.0.1-总指导.md'`.

## What this record is for

This is a prior publication. The public disclosure date above is the date the specification became available to the public.

| Question | Answer |
|---|---|
| Was a patent applied for? | No |
| Why publish? | To place the design in the public domain as prior art, so that no third party can later obtain a patent over it and assert it against this project |
| What is given up? | The right to obtain a patent over the published subject matter in any jurisdiction |
| What is retained? | Copyright, and the licence terms in `LICENSING.md` |

## 中文摘要

| 项 | 值 |
|---|---|
| 公开时刻（UTC） | 2026-10-17T17:44:19Z |
| 首次公开提交 | `3642082ee5e805428e8aa11200555c09f04f3198` |
| 公开时分支 | 仅 `main` |
| 是否申请专利 | 否 |

本记录用于先行公开举证：上述时刻即本规范对公众可见的时刻。

## Document version 1.0.1 — not published

| Item | Value |
|---|---|
| Status | Committed locally only. **Not pushed.** |
| Document version | 1.0.1, merging two text revisions that were never published |
| What changed | Security boundaries made mandatory; TPM/HWID deprecated for removal; the version model reduced to document version plus program version |
| Wire format | Unchanged |
| Effect on the record above | None. Nothing was pushed, so the published commit and hashes stand |

When 1.0.1 is pushed, this section gains the push timestamp and the commit identifier.

## Patents

The maintainers do not seek, and do not intend to seek, patent protection for the
protocol technology described in this repository, in the PRC or anywhere else. The
protocol is published as open documentation and an open implementation, and on the
day of publication the disclosed technology becomes prior art.

Nothing else follows from that. It does not change the licence (CC BY-SA 4.0, see
`LICENSE`), it does not grant or waive rights in the name or mark (see
`TRADEMARK.md`), and it is not a statement about anyone else's patents.

Two limits are worth stating plainly:

- publication only affects filings made **after** it. A filing made earlier is
  unaffected, and the answer to that is a prior-art defence, not this record;
- whether a given disclosure defeats a given claim is a legal question. The
  maintainers record the facts; a lawyer decides what they achieve.

The evidence that makes the record usable is the same evidence listed at the top of
this file: the push timestamp, the commit, the tag, and the content hashes.
