# v0 Protocol Boundaries

SYNTEL v0 is a signed A2A and M2M coordination substrate.

It defines identity references, signed envelopes, bounded task contracts, verification receipts, audit replay, and human escalation hooks.

## In Scope

- agent identity references
- signed message envelopes
- task contracts with explicit constraints
- verification receipts with evidence hashes
- audit/replay semantics
- human escalation on failure
- optional payload extensions for validated artifacts

## Out Of Scope

- autonomous legal contracting
- irreversible settlement by default
- opaque A2A or M2M execution
- public token dependency
- agent marketplace claims
- ITEM canon authority
- ABYS execution orchestration

## Authalien Boundary

Authalien is allowed in SYNTEL only as a signed A2A/M2M payload extension after ITEM has a candidate record and ABYS has a validator task.

SYNTEL does not decide Authalien canon status. It carries bounded payload references, signatures, evidence hashes, and replay metadata.

## Replay Requirement

Every v0 protocol object must be reconstructable from:

1. stable identifier
2. protocol version
3. party or agent references
4. payload reference and hash
5. signature or verifier reference
6. audit trace id
7. replayable flag set to true
