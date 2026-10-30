需要者：提交 PR 的人
不读会错什么：评审要问的问题答不全，PR 会被退回

# 合并请求

本仓是规范性规范。代码与规范分属两个仓，互不拉取，所以在此处的改动是协议变更落地的唯一途径。

## 开单之前

- [ ] **两份镜像都已更新。** `cn/` 与 `en/` 描述同一协议。只改一份属于规范缺陷，不是翻译欠账。
- [ ] 改动已反映在 `isostress-client` 的实现里，或者 PR 明确写明本次只改规范。

- [ ] 版本声明：版本数字是否前进；只换日期段时写出新日期

## 评审会问什么

**你改了规范性取值吗？** 密码套件、密钥派生、帧布局、HKDF 标签、长度上限都是逐字节的表面，两个实现都在测试向量里钉死。此处改规范而实现不改，两边就会打架，只有跨实现测试能抓到。

**你只改了一份镜像吗？** 这是本仓最常见的一类缺陷。开单前两份都查一遍。

**你重编了章节号吗？** 文内交叉引用指向章节号。重编号会让它们静默失效。

**`1.0.0` 还成立吗？** 声明的文档版本号，以及「每个声明的能力都有实现」这句话，必须同时为真。任一项变了，就在 PR 里明说。

## CLA 与关联缺陷

CLA-Agreed: yes

外部贡献者填 yes 表示已读 LICENSING。CI 按整行精确读取本行，大小写与冒号不改。

Fixes #<缺陷编号>

没有关联就写 `Fixes #无`。
---

# Pull requests

This repository is the normative specification. Code and spec are separate
repositories and neither pulls from the other, so a change here is the only way a
protocol change becomes real.

## Before you open

- [ ] **Both mirrors updated.** `cn/` and `en/` describe the same protocol. A change
      present in only one is a specification defect, not a translation debt.
- [ ] The change is reflected in the implementations in `isostress-client`, or the PR says
      explicitly that it is spec-only.

## What reviewers will ask

**Did you change a normative value?** Cipher suite, key derivation, frame layout, HKDF
labels, or length limits are byte-for-byte surface that both implementations pin in
their test vectors. A spec change here without a corresponding implementation change
leaves the two disagreeing, and only the cross-implementation tests will catch it.

**Did you change one mirror only?** That is the single most common defect in this
repository. Please check both before opening.

**Did you renumber a section?** Cross-references inside the document point at section
numbers. Renumbering breaks them silently.

**Is `1.0.0` still accurate?** The declared documentation version, and the statement
that every declared capability has an implementation, must stay true. If either changes, say so
explicitly in the PR.

## CLA and linked issue

CLA-Agreed: yes

An outside contributor writes yes to confirm they have read LICENSING. CI reads this line verbatim.

Fixes #<issue number>

Write `Fixes #none` when the pull request has no linked issue.
