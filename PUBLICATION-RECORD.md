# Publication Record

> Readers: anyone who needs the push time, and anyone who needs to reproduce the content.
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

These are the hashes of the text that tag `pub-2026-10-18` fixes. The working tree has
moved to document version 1.0.2, whose hashes are listed below; the published text stays
retrievable from the tag.

| File | SHA-256 |
|---|---|
| `cn/spec/ZT-DSP-1.0.1-总指导.md` | `0847e4046c6bf9e0b9b799d58709d20d4c063cf97f026f6f9e874f6eddfb26d3` |
| `en/spec/ZT-DSP-1.0.1-Master_Guide.md` | `7824bd19ccbcf29185aa1331b4c87db8a3b8ed477e38bc9cc9504d5dca1c8fd0` |

## How to reproduce

1. Read the timestamps: `gh api repos/ZT-DSP-Suite/ZT-DSP-docs --jq '{createdAt,pushedAt,visibility}'`.
2. Read the published commit: `gh api repos/ZT-DSP-Suite/ZT-DSP-docs/commits/main --jq .sha`.
3. Read the tags: `git ls-remote --tags https://github.com/ZT-DSP-Suite/ZT-DSP-docs.git`.
4. Recompute a hash: `sha256sum 'cn/spec/ZT-DSP-1.0.2-总指导.md'`.
5. Check out the published text: `git checkout pub-2026-10-18 -- cn/spec/ZT-DSP-1.0.1-总指导.md`.

## What this record states

The specification became available to the public at the time recorded above. This file records the facts; it does not argue for any legal effect.

| Question | Answer |
|---|---|
| Was a patent applied for? | No |
| What is given up? | The right to obtain a patent over the published subject matter in any jurisdiction |
| What is retained? | Copyright, and the licence terms in `LICENSING.md` |

## 中文摘要

| 项 | 值 |
|---|---|
| 首次推送（UTC） | 2026-10-17T17:44:19Z |
| 首次公开提交 | `3642082ee5e805428e8aa11200555c09f04f3198` |
| 首次推送时分支 | 仅 `main` |
| 是否申请专利 | 否 |

以上时间与提交用于核对本文件所列内容。

## Document version 1.0.2

| Item | Value |
|---|---|
| Status | Local working tree. Not pushed; awaiting review and a push order. |
| Document version | 1.0.2 |
| Wire format | Unchanged from 1.0.0 |
| Content | `cn/spec/ZT-DSP-1.0.2-总指导.md` `e7815d049eef010565652c0e4b77437fe282651b4ff8d5d78d2336707b8ae0dc`<br>`en/spec/ZT-DSP-1.0.2-Master_Guide.md` `46fa4f75e9b988b64cba7dac046e71608981fb97f34528c692d215ae9442fbd1` |

## Document version 1.0.1

| Item | Value |
|---|---|
| Status | The published text, superseded in the working tree by 1.0.2 |
| Document version | 1.0.1, replacing the text that tag pub-2026-10-18 fixes |
| Wire format | Unchanged from 1.0.0 |
| Content | Fixed by tag spec-1.0.1 |

## Patents

The maintainers do not seek, and do not intend to seek, patent protection for the
protocol technology described in this repository, in the PRC or anywhere else. The
protocol is published as open documentation and an open implementation, and on the
day of publication the described technology is public.

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
