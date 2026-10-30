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

## [1.0.0] - 2026-10-30

### Changed — numbering reset

- **The protocol is named isostress (ISTS).** The cover, the running text and the
  appendices drop the retired name; the subtitle no longer doubles the word "Protocol".
- **Version numbering restarts at 1.0.0.** Development revisions advance only the
  `-YYYYMMDD` segment; a numeric bump happens only on a wire-format change or a
  release. Sections below keep the numbering they were published under.
- **KDF context strings carry the `ISOSTRESS-` prefix.** Derived keys change, and the
  shared vectors were regenerated.

## [1.0.2] - 2026-10-19

### Removed — part of document version 1.0.2

The deprecated hardware key-storage design is gone. No section of the specification
describes storing, binding or writing a key in a TPM or an HWID any more.

- Master Guide 4.1 loses its deprecation block, the two explanatory blocks, the storage
  and property bullets, the nonce true-origin note and the hardware clauses in the
  advice and checklists. The token and the PSK remain, and their storage rules are
  stated plainly in the same subsections.
- The token is **not** affected: the server uses it to identify a device, so every rule
  about it stays. What was removed is the deprecated hardware storage design, not the
  token.
- The glossary entries for the two terms are removed, and the three client READMEs,
  `version.py`, `version.rs`, the PR template, the repository README and
  `CONTRIBUTING.md` drop their notices. Removing a claim that no implementation
  upholds is what makes the remaining claims checkable.

### Added — part of document version 1.0.2

- 5.6 states the deployment conditions that keep a session alive: one reliable ordered
  transport stream, session-affine routing, a fresh handshake on reconnect, and a
  termination count that operators can see.
- The step-1 note under the F.5 pipeline states that the replay check stays exactly as
  written, and that turning it into a silent drop is a protocol change with a version
  bump attached.
- J.4 states that the document version never enters the wire format, and what a version
  mismatch actually looks like to an operator.
- H.3 adds a normative resource bound for the silent hold: three declarations per held
  connection (hold duration, concurrent held-connection count, buffered-byte bound), with
  the hold duration range `(0, 15s]` and a 15 s ceiling that cannot be relaxed.
- C.1 gains three checklist items that record those bound values, and its sequence-number
  line now matches §4.2.3: drop the packet **and** terminate the session.
- F.1 states the response ordering on one connection: the responder's Phase 1 frame
  precedes the next request on that connection, and different connections are not
  ordered against each other.

### Changed — part of document version 1.0.2

The wire format is untouched. Both clients now declare document version 1.0.2 and keep
1.0.0 and 1.0.1 in their declared compatibility list, because the wire format did not
change between those revisions. The document version carries no date suffix.

Statements that the text "has been checked line by line against the reference
implementation" are removed from both mirrors. No baseline commit and no check date were
ever recorded for them, so a reader could not verify what they asserted. The appendices
remain the binding text; dropping an unverifiable claim about that text changes what the
document is allowed to assert, not what it requires.

## [1.0.1] - 2026-10-18

### Deprecated — part of document version 1.0.1

TPM and HWID support is deprecated and will be removed in the next revision.

- Neither reference client, `isostress_py` or `isostress_rs`, contains any code that reads,
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
  plaintext, **MUST NOT** export it, and **MUST NOT** back it up. TPM/HWID storage is
  deprecated and is neither a requirement nor a recommendation; it is kept as a
  record of an earlier design until the next revision removes it. The PSK and the
  token are supplied as ordinary configuration values (`--psk-file` / `--psk-env` /
  `--psk`), keeping them secret is the caller's responsibility, and neither client
  provides hardware-level protection.
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
normative until a later revision ships these:

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