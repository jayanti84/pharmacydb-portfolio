# Business Analysis Approach

## From business question to system behavior

PharmacyDB was used as a practical environment for translating broad analytical goals into explicit system requirements.

The BA approach used in the project can be summarized as:

```text
Business question
    ↓
Scope and evidence boundary
    ↓
Source / stakeholder requirements
    ↓
Current-state process and data flow
    ↓
Business rules and decision points
    ↓
Functional / data requirements
    ↓
Acceptance criteria
    ↓
Implementation and validation
    ↓
Approved read-only output
```

## Example requirements model

| Business need | Requirement | Validation / acceptance evidence |
|---|---|---|
| Trace an analytical value back to evidence | Every governed output must retain source lineage or an approved dependency path | Required provenance fields and dependency checks pass |
| Avoid incorrect product matches | Governed joins must use controlled identifiers rather than name similarity alone | Key and join-authority checks pass; unresolved mappings remain unresolved |
| Protect approved analytical logic | Frozen or approved objects must not be silently mutated | Object definitions and expected hashes/counts are validated |
| Distinguish evidence from interpretation | Direct, derived, proposed, and unresolved states must remain explicit | Method/status fields are preserved and tested |
| Prevent accidental destructive changes | Build processes must reject prohibited operations unless separately authorized | Validators check for prohibited DDL/DML patterns |
| Make ambiguity visible | Unsupported relationships must route to human review | Candidate/unresolved states are excluded from approved downstream views |

## Current-state analysis

The initial problem resembles a common enterprise integration challenge:

- multiple source systems;
- different identifiers and schemas;
- different update schedules;
- duplicated or overlapping concepts;
- varying levels of evidence authority;
- downstream users who need a simpler answer than the source systems provide.

The analysis therefore starts by documenting what already exists before proposing new objects or automation.

One validated schema inventory, for example, reviewed existing objects, columns, view dependencies, source authorities, and overlap candidates before proposing additive changes.

## Future-state principles

The target design follows several business rules:

1. Reuse an existing governed authority when one exists.
2. Add a new object only when the existing model cannot represent the required concept safely.
3. Do not copy canonical data merely to simplify a downstream view.
4. Preserve different business meanings for different dates and evidence types.
5. Keep unresolved relationships explicit.
6. Use read-only downstream views where possible.
7. Require a human decision when evidence does not support deterministic automation.

## Functional decomposition

A large analytical requirement is decomposed into smaller capabilities:

- source discovery and intake;
- source validation;
- identity normalization;
- evidence storage and provenance;
- relationship / bridge management;
- semantic query views;
- release controls;
- deterministic validation;
- exception and human-review handling.

This decomposition makes requirements testable and prevents the implementation from becoming one opaque data pipeline.

## Example acceptance criteria

### Product identity

**Given** a package record is proposed for governed use  
**When** the record enters the controlled identity layer  
**Then** its NDC11 must be represented in the required string format, must satisfy the bounded identity rules, and must not duplicate an existing governed NDC11.

### Unsupported join

**Given** two records have similar manufacturer or product names but no approved identifier relationship  
**When** a downstream mapping is requested  
**Then** the system must not create the relationship automatically and must retain or route an unresolved/human-review state.

### Approved analytical output

**Given** a downstream consumer uses an approved query view  
**When** the view is evaluated  
**Then** proposed or candidate-only fields must not appear in the approved interface.

## Change and impact analysis

Before a schema or workflow change, the project evaluates:

- existing authority for the concept;
- dependencies on the current object;
- downstream views affected;
- key and uniqueness implications;
- provenance and auditability;
- replay/idempotency behavior;
- whether the change is additive or destructive;
- whether human authorization is required.

This is the same reasoning pattern used in enterprise systems analysis: understand the process and dependencies before changing the system.

## BA skills demonstrated

- Requirements analysis
- Functional decomposition
- Process and data-flow mapping
- Current-state / future-state analysis
- Business-rule definition
- Data and integration requirements
- Acceptance criteria
- Impact analysis
- Exception-path design
- UAT-style validation thinking
- Traceability and controlled change
