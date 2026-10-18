# Changelog

All notable changes to this repository are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this
project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

**Note on authority:** this file is a convenience record, not the source of truth. The
authoritative change history is `git log`. If the two ever disagree, `git log` wins.

This repository holds the protocol specification. It ships no test suite — it is a
normative document. What runs mechanically is `scripts/check.py`: it verifies that the
two language mirrors have the same structure, that every relative link resolves, and
that no machine-specific string slipped in.

## [1.0.1] - 2026-10-18

### Deprecated — part of document version 1.0.1

TPM and HWID support is deprecated and will be removed in the next revision.

- Neither reference client, `zt_dsp_py` or `zt_dsp_rs`, contains any code that reads,
  writes or modifies a TPM or an HWID. The earlier wording promised the feature for
  "a later version"; it now says the design is deprecated and will be removed.
- The declaration in Master Guide 4.1.4, the storage and property bullets, the two
  explanatory blocks, and every other TPM/HWID mention now carry a deprecation
  marker, so no reader can mistake the text for a live requirement or advice.
- The client declarations in `version.py` and `version.rs` say the same thing, so the
  specification and the code no longer contradict each other.

### Changed — part of document version 1.0.1

Four security boundaries were advisory and are now mandatory. The wire format is
unchanged, which is why this is a document revision and not a protocol release. The
version model changed in the same revision: the protocol version is withdrawn, and
what used to be called the implementation identifier is now the program identifier,
which carries the program's own version.

- Token and PSK storage: an implementation **MUST NOT** write the token to disk in
  plaintext, **MUST NOT** export it, and **MUST NOT** back it up. Storage in the
  TPM/HWID stays a recommendation, and the reference implementation does not
  implement it.
- Silent drop: the implementation **MUST NOT** write a log entry for a discarded packet.
- Timing: the silent path **MUST NOT** produce a measurable response-time difference
  from the normal path.
- Operators: a server operator **MUST NOT** record the phase one pairing information,
  and **MUST NOT** record correlatable data such as session duration or traffic volume.

### Added

- `CHANGELOG.md`, `CODE_OF_CONDUCT.md`, a pull request template, and `dependabot.yml`
  for GitHub Actions.

### Planned — not part of 1.0.1

Recorded so the intent is not lost. **None of this is implemented**, and 1.0.1 remains
authoritative until a later revision ships these:

- Time-slot driven rotation: one key generation per second rather than per packet.
- Lock packet: the same packet structure, sent on a fixed cadence so the chain keeps
  advancing when there is no message.
- Fragmented key material: the next generation carried as fragments across several
  packets and recoverable from a threshold of them.
- Loss tolerance of 30 slots before the session is declared dead.

The 1.0.0 behaviour is the opposite of the third and fourth items: a single lost packet
leaves the session irreversibly out of step and the only recovery is to reconnect.


## [1.0.0]

- Initial protocol specification, Chinese (`cn/`) and English (`en/`) mirrors.