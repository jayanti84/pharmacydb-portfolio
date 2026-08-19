# PharmacyDB Portfolio

A sanitized portfolio case study showing how I approach business systems analysis, workflow automation, data quality, and governed analytics in a pharmaceutical-data context.

This public repository is intentionally separate from the private implementation repository. It contains no credentials, private cloud identifiers, raw restricted source artifacts, or production secrets.

## What problem does PharmacyDB address?

Pharmaceutical market and product questions often require evidence from multiple public sources that were not designed to work together. Pricing, product identity, regulatory events, and financial context may use different identifiers, update cycles, and levels of detail.

The project explores how to turn those disconnected sources into a controlled analytical workflow by making source authority, identity, provenance, validation, and human-review boundaries explicit.

## Business analysis view

The project is structured around a repeatable BA workflow:

1. Define the business question and scope.
2. Identify authoritative source systems and limitations.
3. Map current-state data flows and dependencies.
4. Define governed identities, joins, and business rules.
5. Translate requirements into data models, workflows, and validation rules.
6. Test outputs against acceptance criteria.
7. Publish only approved, read-only analytical views.
8. Route ambiguous mappings or unsupported conclusions to human review.

## High-level architecture

```mermaid
flowchart LR
    A[Public pharmaceutical and corporate sources] --> B[Acquisition and source-specific adapters]
    B --> C[Validation, provenance, normalization]
    C --> D[Governed evidence layer]
    D --> E[Semantic and query layer]
    E --> F[Read-only analytics and bounded AI interfaces]

    G[Human review] --> C
    G --> D
    G --> E
```

Example source domains include public pricing benchmarks, FDA regulatory data, product/package identity data, and controlled financial evidence.

## What this project demonstrates

- Business requirements analysis and functional decomposition
- Current-state and future-state process thinking
- Data-source authority and provenance controls
- Product and package identity governance
- SQL and data-model design
- Python-based validation and automation
- API and workflow integration concepts
- Deterministic testing and replay checks
- Read-only semantic/query layers
- Human-review gates for ambiguous mappings
- Fail-closed behavior when authority or identity is insufficient

## Verified project scale snapshot

One validated schema inventory in the private implementation documented:

- 4 named target datasets available
- 76 target data objects
- 1,739 live columns
- 38 parsed view dependencies
- a governed 48-package NDC11 identity set with no duplicate or invalid NDC11 values in that bounded set

These figures describe a validated project snapshot, not a claim of full-market coverage.

## Technology evolution

The project evolved through several implementation stages rather than starting with one fixed architecture.

| Area | Technologies / approach |
|---|---|
| Data acquisition and automation | Python, APIs, web-based source intake, workflow automation concepts including n8n |
| Earlier application/data layer | PostgreSQL, FastAPI |
| Current governed analytical layer | Google BigQuery, SQL, structured evidence and semantic views |
| Validation | Python tests, deterministic validators, hashes, replay and schema checks |
| Delivery discipline | Git, GitHub, controlled changes, documented acceptance and release boundaries |

Earlier technologies are retained as project history; they are not represented here as a single live production stack.

## Recruiter review path

For a short review of the project:

1. [Business case and solution approach](docs/CASE_STUDY.md)
2. [Business analysis artifacts and decision model](docs/BUSINESS_ANALYSIS.md)
3. [Sanitized architecture and process maps](docs/ARCHITECTURE.md)
4. [Validation, UAT-style scenarios, and defect triage](docs/VALIDATION.md)
5. [Sanitized SQL example](examples/governed_view_example.sql)
6. [Sanitized Python validation example](examples/validate_identity_example.py)

## Code examples

The `examples/` directory contains deliberately small, sanitized examples that demonstrate technical literacy without copying private production-style implementation into the public portfolio.

- `governed_view_example.sql` demonstrates an approved read-only view pattern and a duplicate-key validation query.
- `validate_identity_example.py` demonstrates deterministic NDC11 format and uniqueness validation using synthetic test values.

## Portfolio boundary

This repository is a professional case study, not a production pharmaceutical system. It does not provide clinical, prescribing, reimbursement, or autonomous decision support. It also does not expose the private implementation repository or its controlled source artifacts.
