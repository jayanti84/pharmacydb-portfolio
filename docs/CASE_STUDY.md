# PharmacyDB Case Study

## Context

Pharmaceutical pricing and market analysis frequently depends on multiple public datasets that differ in identifiers, granularity, timing, terminology, and source authority.

A useful analytical system therefore needs more than data ingestion. It needs explicit rules for what each source can prove, how records may be joined, when data is considered validated, and when a human decision is required.

## Business problem

The project was framed around six bounded analytical question areas covering pricing relationships, financial context, regulatory evidence, corporate context, market comparators, and loss-of-exclusivity/event analysis.

The core systems problem was consistent across those questions:

> How can multiple external evidence sources be organized so that downstream analysis is traceable, repeatable, and resistant to unsupported joins or conclusions?

## Requirements identified

The solution needed to support the following capabilities:

- preserve source provenance and evidence lineage;
- normalize package/product identifiers without silently inferring identity;
- distinguish direct evidence from derived or interpreted outputs;
- keep source-specific dates and meanings separate;
- prevent unsafe name-only joins;
- expose analytical outputs through controlled, read-only views;
- make missing or unresolved evidence visible instead of filling gaps with guesses;
- provide deterministic validation and repeatability checks;
- retain human approval for ambiguous entity, product, application, and event mappings.

## Solution approach

### 1. Source intake

Public evidence is collected from source domains such as pharmaceutical pricing benchmarks, FDA regulatory datasets, product/package identity sources, and corporate/financial filings.

Each source is treated according to its own authority and limitations rather than being flattened immediately into one generic dataset.

### 2. Governed identity

Package and product identity is controlled through explicit identifiers. One validated inventory documented a bounded 48-package NDC11 authority with no duplicate or invalid NDC11 values in that set.

Where an identity cannot be proven from a controlled key, the workflow preserves the unresolved state rather than matching by name alone.

### 3. Evidence and semantic layers

Source evidence is separated from downstream semantic/query views. This allows analytical views to reuse governed evidence without creating competing copies of canonical data.

### 4. Validation

Validation is treated as a design requirement rather than a final testing step. Controls include schema checks, key uniqueness, lineage requirements, prohibited-operation checks, dependency checks, and replay/repeatability tests.

### 5. Human decision gates

Some relationships cannot be safely automated. Examples include ambiguous manufacturer/entity relationships, biosimilar/reference mappings, and event-to-product mappings. These are explicitly routed to human review.

## Example decision rule

A key project rule is:

> Use controlled identifiers for joins; do not infer a governed relationship from similar names alone.

This converts a broad data-quality concern into a testable functional requirement.

## Outcome

The project produced a governed analytical structure in which business questions, source authority, identity rules, validation controls, and downstream views are separated but connected.

A validated architecture inventory documented 76 target objects, 1,739 live columns, and 38 parsed view dependencies across four named target datasets. The portfolio presents these figures only as a bounded project snapshot.

## What I learned as a Business Systems Analyst

The strongest lesson from the project is that a technical solution is only useful when its decision rules are explicit.

For a BA, that means asking:

- What business question are we actually answering?
- Which system or source is authoritative for each field?
- What happens when two sources disagree?
- Which joins are allowed?
- What constitutes an acceptable result?
- What must remain unresolved?
- What requires human approval?
- How will the solution be tested and reproduced?

Those questions drive the process model, functional requirements, acceptance criteria, and system design.

## Scope and limitations

This is an independent portfolio and learning project. It is not represented as a production pharmaceutical, clinical, reimbursement, or autonomous decision system. The public repository intentionally omits private implementation details, source archives, credentials, and cloud identifiers.
