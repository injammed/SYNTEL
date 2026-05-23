# Future Note: VMS Metadata for SYNTEL

## Purpose

This is not a v0 priority. It is a future compatibility note.

If ITEM currency artifacts later need representation in inter-agent exchange contexts, SYNTEL should support metadata fields that preserve VMS class and issuance semantics without importing visual doctrine into the protocol layer.

## Scope

Future protocol metadata may include:

- currency_unit_name
- vms_class
- issuance_type
- denomination_relation
- artifact_id
- provenance_reference
- settlement_mode
- reversibility_flag

## Constraint

SYNTEL must not become a speculative currency layer.

This note exists only to preserve future interoperability.

## Rule

Only encode what is needed for:

- reference
- exchange context
- auditability
- receipt semantics

Do not import ITEM visual language or ceremonial ontology directly into v0 protocol logic.
