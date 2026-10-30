# Publication Record

> Readers: anyone who needs the push time, and anyone who needs to reproduce the content.
> Status: current.

## What was published

| Item | Value |
|---|---|
| Repository | `https://github.com/isostress-suite/isostress-docs` |
| Visibility | PUBLIC |
| Created (UTC) | 2026-10-17T17:43:46Z |
| Last pushed (UTC) | 2026-10-27T00:54:20Z (`gh api repos/isostress-suite/isostress-docs --jq .pushed_at`) |
| Default branch | `main` |
| First public commit | `3642082ee5e805428e8aa11200555c09f04f3198` |
| Release tag | `pub-2026-10-18` → `3642082` (annotated) |
| Earlier tag | `docs-v1.0.0` → `837bfb8d1c468e0a25b60a448915879c47c3ae1e` (annotated) |
| 1.0.1 tag | `spec-1.0.1` → `676fa397f3cfe0db58f7c5184967c9d1b29b3179` (annotated) |
| Branches at publication | `main` only (state on 2026-10-17; current branches: `gh api repos/isostress-suite/isostress-docs/branches`) |
| Facts verified at (UTC) | 2026-10-27T19:14:53Z (re-verified after the program-identifier separator fix) |
| Evidence commands | `gh api repos/isostress-suite/isostress-docs --jq '{created_at,pushed_at,visibility}'` · `gh api repos/isostress-suite/isostress-docs/commits/main --jq .sha` · `git hash-object <file>` · `sha256sum <file>` · `git rev-parse '<ref>:<path>'` · `git show '<ref>:<path>' \| sha256sum` |

## Content hashes

Each row is one published text. Blobs are read with `git hash-object` (or
`git rev-parse <ref>:<path>`); SHA-256 with `sha256sum`. Every value below was recomputed
on 2026-10-27T15:40:22Z; the four `1.0.2 working tree` values were recomputed again on
2026-10-27T15:43:08Z after the S1-S4 wording fix, once more on 2026-10-27T16:07:44Z after
the H.3/C.1 repair, once more on 2026-10-27T16:24:46Z after the W2 wording sweep, once more on
2026-10-27T16:53:58Z after the R2 follow-ups, and once more on 2026-10-27T19:14:53Z after the
program-identifier separator fix (see Revision history), none is copied from an earlier version of this file.
The `1.0.2 working tree` rows are the text after the A-tier fix of the "no server
implementation" claims and the appendix list, plus the S1-S4 wording fix (arbitration
S1-S4: sequence-number handling, silent-drop close scope, log classes, modal alignment),
plus the H.3/C.1 repair (misconception paragraph restored, resource-bound block split into
its own paragraph, `C.1` aligned with `4.2.3`, three silent-hold bound items added),
plus the W2 wording sweep (Rev 4: `CODE_OF_CONDUCT` adverb, auth trademark sentences,
the two English-guide CLI mentions, the `CHANGELOG` rule wording);
they stay behind the `published` rows
until the next push, then both rows converge. The `1.0.2 working tree` group expires with
the next text change: whoever edits either 1.0.2 spec file recomputes those four values
before handing the work over.

| Version | File | Git blob | SHA-256 |
|---|---|---|---|
| 1.0.0 (tag `pub-2026-10-18`) | `cn/spec/ZT-DSP-1.0.0-总指导.md` | `5e073282232d723682edef9ea5b3056e22b18882` | `0847e4046c6bf9e0b9b799d58709d20d4c063cf97f026f6f9e874f6eddfb26d3` |
| 1.0.0 (tag `pub-2026-10-18`) | `en/spec/ZT-DSP-1.0.0-Master_Guide.md` | `48dcda44d3e923adea9eb173640e919ca8621552` | `7824bd19ccbcf29185aa1331b4c87db8a3b8ed477e38bc9cc9504d5dca1c8fd0` |
| 1.0.1 (tag `spec-1.0.1`) | `cn/spec/ZT-DSP-1.0.1-总指导.md` | `4efbc20840603681bcd8bef33a4752bebb5a3f75` | `cf497f4660320d548655ff6c4a22f0c905beff1f6becb5d59d191267ccb9240d` |
| 1.0.1 (tag `spec-1.0.1`) | `en/spec/ZT-DSP-1.0.1-Master_Guide.md` | `ac319af16c03c7414f9a6b67a18666e519c7ad1f` | `7696acf990146f7f3251f5244365d4957fb27fc2bf8c616586312973600eac4a` |
| 1.0.2 published (in `main` `e47babf`) | 中英规范文本存于该提交，无 tag；被本次 1.0.0 重置取代，校验值不再保留 |
| 1.0.0 reset (unpushed) | `cn/spec/isostress-1.0.0-总指导.md` | `8eaf276123ac5be1c781a5c2cee36b798927b1da` | `00f3c61d8e2c752be4f3737a38c25e72bbe525cfd107dd58bcf7564797f2396d` |
| 1.0.0 reset (unpushed) | `en/spec/isostress-1.0.0-Master_Guide.md` | `61316fbd8c1b902f1c00e772312e3b3f7b5ff2b3` | `0d69b10484bc1d6a21bab9e53595d3f4e1bee159fafce66190b7b8205fa37ba6` |

## Revision history of this record

| Rev | When (UTC) | Change | Superseded values (kept for audit) |
|---|---|---|---|
| 1 | 2026-10-27T15:40:22Z | Corrected the `1.0.0`/`1.0.1` labels; recomputed the `1.0.2 published` rows; added the `1.0.2 working tree` group | The two `1.0.2` rows previously carried `177a976d…`/`5c48ed7e…` (content of the 2026-10-20 draft revisions `0f6675f`/`5ea59a4d`, not of the published text) |
| 2 | 2026-10-27T15:43:08Z | Re-fixed the two spec files per arbitration S1-S4 (sequence-number handling, silent-drop close scope, log classes, modal alignment) and recomputed the four `1.0.2 working tree` values | cn blob `5d02555325c4aa15176f40e485f4f499a517ba34` / SHA-256 `bc5b8a40d3880359c293964cb89a7ca5ac5d2a80283c52eb501a8aabd649d6d8`; en blob `254e70629675748134ba8c57bb8b1e749d002288` / SHA-256 `a111abdc8180acea5a8a4fee85b8f710dc953eb49a6f21037bc81934c9b9c8ae` |
| 3 | 2026-10-27T16:07:44Z | Restored the split `H.3` misconception paragraph (the resource-bound block is now its own paragraph), aligned `C.1` with `4.2.3` (drop **and terminate**), added the three silent-hold bound items to `C.1`, and merged the split trademark sentence in `TRADEMARK.md`; recomputed the two `1.0.2 working tree` values | cn blob `69fb7d1f5e1e3ca5c660bc82ddbb432f8ed71b2c` / SHA-256 `d2a508923d92d6b33d291d49c55cbfee8b63e71cd00a08b1720289116eb6e0a9`; en blob `4ac2ecf0ccf78357800aa414d1643f3983bc0aac` / SHA-256 `1389159c92d1753132e6e5230b13294a28f7e13d047b9c029e049323e5948954` |
| 4 | 2026-10-27T16:24:46Z | Swept the remaining `official→published` mechanical-replace damage reported by W2: the `CODE_OF_CONDUCT` adverb restored to `officially`, the auth trademark prohibition and distribution sentences restored, and the two English-guide CLI mentions changed to `reference CLI` (matching the Chinese text); unified the three `CHANGELOG` rules to `authoritative change history is git log`; recomputed the two `1.0.2 working tree` values | cn blob `16adabfc926e50ead10b4a93fe0e0c131e4e7e0c` / SHA-256 `bb5a477a6dbfd1432243b0b85e77b5ff32ef8a8c0dc5132ab5db3f5b794bda7f`; en blob `873408993a74fb95a5941405b42e60fe156e1256` / SHA-256 `7d67def66ad55c82c3308751f8d750a078f40a05d87d9689159b6f971c81c513` |
| 5 | 2026-10-27T16:38:28Z | Documentation-only correction in this record: the `## Document version 1.0.2` summary still quoted the pre-Rev-4 English working-tree pair; replaced with the authoritative pair from the Content hashes table, aligned the `数值核实时间` field with `Facts verified at`, and appended the W2 step to the recomputation narrative. No spec file changed in this revision; all four `1.0.2 working tree` values were recomputed and are unchanged | (none) |
| 6 | 2026-10-27T16:53:58Z | R2 follow-ups: H.3 hold duration now states the range `(0, 15s]` and the non-relaxable 15 s ceiling, and the three `C.1` bound items are marked as normative additions in the three `CHANGELOG` files; the `TRADEMARK` referent is now `Those names identify the isostress project.` and the Chinese prohibition list is restored to the official/reference/canonical wording with `等官方包名`; recomputed the two `1.0.2 working tree` values | cn blob `16adabfc926e50ead10b4a93fe0e0c131e4e7e0c` / SHA-256 `bb5a477a6dbfd1432243b0b85e77b5ff32ef8a8c0dc5132ab5db3f5b794bda7f`; en blob `86edcf6b907b7c58dbc74642758081239e2a0c3f` / SHA-256 `632be8686543109451d4f0b94ba8835d342c1200c8d3eb968fcf827e3cc39788` |
| 7 | 2026-10-27T17:43:12Z | **Renumbered:** previously numbered 8 while its timestamp preceded the row now numbered 8; the two rows were reordered by timestamp. Recomputed the `1.0.2 working tree` group after the R-D2 fixes to the spec pair (FAQ count 15→16 in both languages; C22 blank line before the Appendix B heading in both files): both `cn` and `en` changed. Values re-derived by `git hash-object` (blob) and `sha256sum` on the working tree; the `1.0.2 published` rows still anchor `main` `e47babf` | `cn` previously `e1ad8a0f…` / `5b263850…`; `en` previously `ca02da22…` / `69c5acb4…` |
| 8 | 2026-10-27T17:45:00Z | **Renumbered:** previously numbered 7 and placed above the earlier entry; now ordered after it. Recomputed the `1.0.2 working tree` group after the W2/R2 spec edits: `en` changed, `cn` unchanged. Both rows of the group were re-derived by `git hash-object` (blob) and `sha256sum` (SHA-256) on the working tree; the `1.0.2 published` rows stay at `main` `e47babf` | `en` working tree previously `9fa16a28…` / `d6e0e728…` |
| 9 | 2026-10-27T19:14:53Z | Fixed the program-identifier separator inconsistency (A2/D1 P1): the template in `0.1` and `J.4` now reads `<语言>-<版本>[-<YYYYMMDD>]` / `<language>-<version>[-<YYYYMMDD>]`, matching every example, the `J.5` registry and the three implementations; the "separator is a single underscore" sentence is replaced by "a hyphen separates the language token from the version" (no second convention left). Refs in `CONFORMANCE-GUIDE`, `DEV-GUIDE`, `Glossary` and the term table were out of that card's scope at the time; the underscore form was removed by t88 (verified 2026-10-27T20:38Z: `grep -rn '<语言>_\|<language>_'` returns 0 on both guides, the DEV-GUIDE pair and the glossary). Recomputed the two `1.0.2 working tree` values | cn blob `813f999703f15a949b1296ab84668b15184e1066` / SHA-256 `424b32f3e6763be10c7ea97f4aec5231e10462473545f280f3aed2251748c280`; en blob `06824b8862cfacead75848a376235b477b82d97e` / SHA-256 `73c35ba4ae86b84f388e5568486160343350d63823eef5440da537b7d3638337` |
| 10 | 2026-10-27T20:38:10Z | Record-only corrections from the breadth-first audit (A7): (a) `Rev 7` and `Rev 8` were numbered against timestamp order — both are renumbered by timestamp and each row records its former number; (b) the `Rev 9` note about the guides and glossary is updated to the current state (underscore form removed by t88). The four `1.0.2 working tree` values were re-derived by `git hash-object` and `sha256sum` and match the table | none (values unchanged) |
If a future edit touches either 1.0.2 spec file, add a new row here and recompute the
group again; never overwrite the superseded values.

## How to reproduce

Run every step inside `isostress-docs/`. Each step exits 0 as written; none writes to the
worktree. All seven steps were executed on 2026-10-27T15:40:22Z with exit code 0, and
re-executed on 2026-10-27T15:43:08Z after the S1-S4 fix (same exit code).

1. Read the timestamps: `gh api repos/isostress-suite/isostress-docs --jq '{created_at,pushed_at,visibility}'`.
2. Read the published commit: `gh api repos/isostress-suite/isostress-docs/commits/main --jq .sha`.
3. Read the tags: `git ls-remote --tags https://github.com/isostress-suite/isostress-docs.git`.
4. Recompute a blob hash: `git hash-object cn/spec/isostress-1.0.0-总指导.md`.
5. Recompute a SHA-256: `sha256sum 'cn/spec/isostress-1.0.0-总指导.md'`.
6. Read the 1.0.0 text without touching the worktree: `git show 'pub-2026-10-18:cn/spec/isostress-1.0.0-总指导.md' | sha256sum`.
7. Read the 1.0.1 text: `git show 'spec-1.0.1:cn/spec/ZT-DSP-1.0.1-总指导.md' | sha256sum`.

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
| 创建（UTC） | 2026-10-17T17:43:46Z |
| 最近推送（UTC） | 2026-10-27T00:54:20Z |
| 首次公开提交 | `3642082ee5e805428e8aa11200555c09f04f3198` |
| 发布当时分支 | 仅 `main` |
| 数值核实时间（UTC） | 2026-10-27T19:14:53Z（与 Facts verified at 同一时刻；程序标识分隔符修订后重算并全表复核） |
| 是否申请专利 | 否 |

以上时间与提交用于核对本文件所列内容。

## Document version 1.0.2

| Item | Value |
|---|---|
| Status | Pushed. In `main` at `e47babf18a14780a0967993e6e43949e8d2edf37`; last push (UTC) 2026-10-27T00:54:20Z from `gh api`. No tag yet. |
| Document version | 1.0.2 |
| Wire format | Unchanged from 1.0.0 |
| Content | published blob/SHA-256 `cdddf7f1…` / `b72cdf02…` (cn), `5aa40921…` / `7c579c34…` (en); working tree after the S1-S4 fix, the H.3/C.1 repair, the W2 wording sweep, the R2 follow-ups, the Rev 7/Rev 8 recomputes after the R-D2 count/C22 fixes, and the Rev 9 program-identifier separator fix (Rev 4-9) `2b9a63ab…` / `6c2420f9…` (cn), `c71ca1e9…` / `deccd23c…` (en). Full values in Content hashes; superseded values stay in the revision history. |

## Document version 1.0.1

| Item | Value |
|---|---|
| Status | Superseded by 1.0.2; text fixed by tag `spec-1.0.1` |
| Document version | 1.0.1, superseding the 1.0.0 text that tag `pub-2026-10-18` fixes |
| Wire format | Unchanged from 1.0.0 |
| Content | `cn/spec/ZT-DSP-1.0.1-总指导.md` blob `4efbc20840603681bcd8bef33a4752bebb5a3f75` / SHA-256 `cf497f4660320d548655ff6c4a22f0c905beff1f6becb5d59d191267ccb9240d`<br>`en/spec/ZT-DSP-1.0.1-Master_Guide.md` blob `ac319af16c03c7414f9a6b67a18666e519c7ad1f` / SHA-256 `7696acf990146f7f3251f5244365d4957fb27fc2bf8c616586312973600eac4a` |

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
