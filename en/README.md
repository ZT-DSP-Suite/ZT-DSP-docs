# isostress Protocol Documentation

## 这里有什么

The English specification and the glossary.

## 按什么找

The full map is in the [repository README](../README.md).

> The specification for the current protocol. The normative text is `en/spec/isostress-1.0.0-Master_Guide.md` (docs version 1.0.0).
>
> **How this repository relates to the implementations**: the specification defines the protocol behaviour and tunable parameters; each implementation declares at its entry point which guide it applies to, and each guide lists the client and server versions it applies to. The relation is **many-to-many**, not bound by version numbers.

This repository carries **documentation only**; the reference implementations and runtime code live in the separate `isostress-client` repository.

> The full document map, grouped by what you want to do, is in the [repository README](../README.md).

## Layout

```
isostress-docs/
├─ README.md                 this index
├─ LICENSE                   full text of CC BY-SA 4.0
├─ LICENSING.md              license scope, attribution and trademarks
├─ CONTRIBUTING.md           contributor license agreement
├─ SECURITY.md               security policy and vulnerability reporting
├─ CITATION.cff              citation metadata
├─ cn/                       Chinese side
│  ├─ spec/isostress-1.0.0-总指导.md      the specification (the only current revision)
│  ├─ 术语对照表.md                    Chinese-to-English terminology baseline
├─ en/                       English side (mirrors cn/ document by document)
│  ├─ spec/isostress-1.0.0-Master_Guide.md
│  ├─ Glossary.md
└─ .github/                  issue forms and the Pages workflow
```

## spec/ — the specification

The current revision is **docs 1.0.0**, and it is the **only** specification file this repository carries. It applies to the client versions `ISOSTRESS_PY-1.0.0` / `ISOSTRESS_RS-1.0.0` and to the server version `ISOSTRESS_SV-1.0.0` (Rust implementation in `isostress-server/src/`; Python reference implementation `ISOSTRESS_SV-1.0.0-20261030` in `isostress-client/isostress_sv_py/`).

| File | Content |
|------|---------|
| `cn/spec/isostress-1.0.0-总指导.md` | **Protocol Master Guide** (Chinese side). Book Four core protocol, Appendix B parameters, Appendix C implementation checklist, Appendix F byte-level on-wire specification, Appendix G traffic-defence details, Appendix H state machine and timeout matrix. |
| `en/spec/isostress-1.0.0-Master_Guide.md` | The same, on the English side. |

## Bilingual mirroring

`cn/` and `en/` correspond document by document. **A one-sided change is a defect**, not a contribution.

## Terminology baseline

| File | Purpose |
|------|---------|
| `cn/术语对照表.md` | Chinese-to-English terminology baseline |
| `en/Glossary.md` | English-to-Chinese terminology baseline |

These two files are the single normative source of terminology.

## Versions

The project has **three kinds of version number** and one **two-way declaration** between documents and implementations:

- **total-guide version (1.0.0)** — the revision number of this documentation repository, written `docs 1.0.0`. It never appears on the wire.
- **client version** — the full identifier of a client implementation, `isostress_<language prefix>-<major.minor.patch>` — `ISOSTRESS_PY-1.0.0` for Python, `ISOSTRESS_RS-1.0.0` for Rust. Implementations in different languages may share a version number and are distinguished by the prefix.
- **server version** — the full identifier of a server implementation, `ISOSTRESS_SV-1.0.0`. `SV` is a role prefix, not a language prefix. Rust implementation in `isostress-server/src/`; Python reference implementation `ISOSTRESS_SV-1.0.0-20261030` in `isostress-client/isostress_sv_py/`.
- **Two-way declaration** — the document side (the head of `spec/`) lists **the client and server versions to which it applies** and declares which settings it governs; the implementation side (`FOLLOWS_DOC` and `APPLIES_TO_DOC_VERSIONS` in `isostress_py/version.py`) declares which document it applies to. **The two are not bound by version numbers.**

**Applicability is many-to-many, not one-to-one**: several implementations of the same kind whose protocol behaviour has not changed share one applicability declaration, and the same guide may apply to several client and server versions at once. **Identical version numbers do not mean the same implementation and do not constitute a compatibility claim.**

**No version string travels in the handshake frames**: neither the phase-one parameter JSON nor the phase-four AAD carries a version or protocol identifier. Whether the peer follows the same document is settled by the phase-three confirmation tag.

**The current revision rules**: implementations are judged against Appendix F (byte-level on-wire specification) and Appendix H (state machine and timeout matrix).

## Repository boundary

- **This repository (isostress-docs)**: protocol specification, terminology baselines, design assets, repository configuration.
- **The code repository (isostress-client)**: the reference implementations `isostress_py/` (Python) and `isostress_rs/` (Rust), plus run scripts and engineering files.
- **The server side**: `isostress-server/` (Rust, `ISOSTRESS_SV-1.0.0`) and `isostress-client/isostress_sv_py/` (Python reference implementation, `ISOSTRESS_SV-1.0.0-20261030`). The identifier form `ISOSTRESS_SV-<major.minor.patch>` is in use.
- Paths such as `isostress_py/` and `isostress_rs/` appearing in the documentation refer to the reference implementation directories **inside the code repository**, not to this one.
- Nothing is carried across: documentation changes go here, code changes go to the code repository, server changes go to the server repository.

## Licence

The specification text in this repository is licensed under **CC BY-SA 4.0**. See [LICENSING.md](../LICENSING.md) and [LICENSE](../LICENSE).
