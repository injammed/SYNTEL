# Trust And Failure Model

SYNTEL v0 assumes agents can fail, keys can rotate, payloads can be malformed, and business intent can be ambiguous.

The protocol is designed to preserve evidence and support replay, not to make opaque autonomous decisions final.

## Trust Inputs

- registry-backed agent identity
- sender and recipient organization references
- signed envelope hashes
- bounded task contracts
- verification receipts
- human escalation contacts
- replayable audit traces

## Failure Classes

| Failure | Required result |
|---|---|
| invalid signature | reject and record audit event |
| unknown identity | hold for human review |
| expired envelope | reject or request resend |
| payload hash mismatch | reject and open dispute path |
| task scope ambiguity | escalate to human |
| failed verification | emit failed receipt with evidence |
| Authalien payload without ITEM/ABYS gate | reject as unvalidated extension |

## Settlement Rule

SYNTEL v0 does not finalize irreversible settlement by default. Receipts may close coordination loops, but settlement adapters are future work and must remain outside v0 default behavior.

## Human Escalation

Human escalation is not a failure of the protocol. It is the safety valve that prevents vague, high-risk, or disputed agent coordination from becoming opaque execution.
