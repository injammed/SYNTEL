# SYNTEL Protocol Triage Rubric

## Purpose

This rubric prevents SYNTEL from becoming vague agent-market rhetoric. SYNTEL only keeps material that can become a bounded, auditable, machine-readable coordination rail.

## Scoring model

Score each SYNTEL fragment from 0-2 in each category.

| Category | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Party definition | No parties | Parties implied | Sender, receiver, authority, and human escalation role named |
| Identity/auth | No proof | Identity mentioned | Verification, signing, authorization, and trust assumption specified |
| Message shape | Pure prose | Fields implied | Concrete envelope, schema, endpoint, state, or test vector named |
| Constraint boundary | Open-ended autonomy | Some limits | Bounded task, allowed actions, expiry, failure mode, and reversibility specified |
| Verification/audit | Outcome assumed | Receipt mentioned | Receipt, replay trail, audit log, and conformance test specified |
| Repo boundary | Mixes canon/execution/protocol | Mostly protocol | Clearly protocol-only; implementation goes to ABYS and artifacts to ITEM |

## Decision thresholds

- 10-12: promote into `/spec`, `/examples`, `/tests`, or protocol architecture docs.
- 7-9: keep as draft protocol work and assign schema/test-vector refinement.
- 4-6: compress into a narrow issue or reroute to ITEM/ABYS.
- 0-3: delete, archive, or defer as marketplace/token/autonomy slop.

## Hard fail conditions

A fragment fails immediately if it:

- Claims autonomous coordination without identity, authorization, audit, replay, or human interruption.
- Mentions settlement before bounded task contracts and reversible failure modes exist.
- Depends on public tokens for the MVP rail.
- Describes artifacts instead of transmitting artifact records from ITEM.
- Describes implementation workflow instead of protocol contracts for ABYS to implement.

## Upgrade pattern

Every salvageable SYNTEL fragment should be rewritten into this minimum protocol brief:

```md
# Protocol element name

## Status
candidate | spec | deprecated

## Parties
Who sends, receives, authorizes, observes, and escalates?

## Identity and trust
How are parties identified, verified, authorized, and constrained?

## Message shape
What envelope, fields, signatures, timestamps, and payloads exist?

## State transition
What states can the interaction enter, and what transitions are valid?

## Verification and audit
What receipt, log, replay, or conformance test proves what happened?

## Failure and interruption
How does the system fail safely or hand off to a human?

## ABYS handoff
What validator, mock server, client, test harness, or reference implementation should ABYS build?

## ITEM handoff
What artifact records can be carried as payloads without importing ITEM doctrine into protocol core?
```

## Better configuration ruling

SYNTEL should be the downstream coordination rail: it transmits structured intent, capability, obligation, receipt, and audit data. Its higher capability comes from boring trust: signed envelopes before markets, receipts before settlement, human escalation before autonomy.
