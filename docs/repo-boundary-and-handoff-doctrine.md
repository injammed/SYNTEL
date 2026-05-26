# SYNTEL Boundary and Handoff Doctrine

## Role

SYNTEL is the downstream coordination rail for bounded A2A/M2M communication. It specifies how agents identify parties, exchange signed messages, negotiate constrained intent, verify outcomes, produce receipts, replay audits, and escalate to humans.

SYNTEL does not preserve artifact meaning and does not own execution workflow.

## Keep

Keep material that can become one of the following:

- agent identity registry rule
- signed message envelope
- capability discovery endpoint
- bounded intent negotiation protocol
- task contract format
- verification receipt format
- audit log or replay rule
- human escalation hook
- protocol conformance test vector

## Delete, deprecate, or refactor

Flag material for deletion or refactor when it:

- claims autonomous coordination without identity, authorization, audit, replay, bounded action, and interruption
- describes markets, public tokens, settlement, or irreversible exchange before task contracts and receipts exist
- imports ITEM artifact doctrine into protocol core
- imports ABYS implementation workflow into protocol specification
- uses agent-market rhetoric without a concrete message shape, state transition, or conformance test

## Handoff contracts

### SYNTEL -> ABYS

A protocol element must tell ABYS what validator, mock server, client, integration test, replay tool, or reference implementation should be built.

### SYNTEL -> ITEM

A protocol element may carry ITEM artifact records as payloads, object references, registry entries, or receipt attachments. It must not redefine the artifact's meaning.

## Protocol rule

SYNTEL gains power through boring trust. Signed envelopes before markets. Receipts before settlement. Escalation before autonomy.
