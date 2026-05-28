# SYNTEL

SYNTEL is a signed A2A and M2M coordination protocol.

It defines identity, signed envelopes, bounded task contracts, verification receipts, and audit replay semantics for agents that need to coordinate across systems or organizations.

SYNTEL v0 is the boring trust rail first. Nothing mystical. Nothing autonomous by default.

## Core Thesis

Enterprises will deploy agents internally before they trust open agent markets. The hard problem is safe coordination: one agent proving identity, expressing bounded intent, accepting constraints, producing evidence, and leaving a replayable audit trail.

## v0 Substrate

The initial SYNTEL substrate provides:

1. Agent identity references
2. Signed message envelopes
3. Task contract format
4. Verification receipt format
5. Audit log and replay semantics
6. Human escalation hooks
7. Optional payload extensions, including validated ITEM artifacts such as Authalien candidates

## Non-Goals For v0

- No autonomous legal contracting
- No irreversible settlement by default
- No opaque A2A or M2M execution
- No public token dependency
- No agent marketplace claims
- No protocol authority over ITEM canon or ABYS execution

## Repository Structure

```txt
/docs      Protocol boundaries, trust model, failure model
/spec      Machine-readable protocol specifications
/examples  Example signed envelopes and receipts
/src       Future reference implementation
/tests     Future protocol and integration tests
```

## Build Direction

SYNTEL should start as a narrow, trustworthy protocol service.

```txt
agent identity
-> signed envelopes
-> bounded task contracts
-> verification receipts
-> audit replay
-> human escalation
```
