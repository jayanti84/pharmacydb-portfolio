# Validation and Acceptance Approach

## Why validation is part of the design

In PharmacyDB, validation is not treated as a final QA step. Business rules are converted into checks that can be repeated whenever a controlled package changes.

The private implementation includes deterministic validators for schema authority, source lineage, controlled identifiers, prohibited operations, dependencies, release conditions, and repeatability.

## Validation layers

### 1. Source validation

Questions include:

- Is the source the intended authority for this fact or identifier?
- Is the source version/date known?
- Is provenance preserved?
- Is a record missing, malformed, or unresolved?

### 2. Identity validation

Controlled identity checks include:

- required identifier format;
- key uniqueness;
- duplicate detection;
- bounded source provenance;
- explicit unresolved status where identity cannot be proven.

A validated project snapshot documented a bounded 48-package NDC11 set with no duplicate or invalid NDC11 values.

### 3. Schema and dependency validation

The system validates expected objects and fields before downstream use. One validated inventory documented 76 target objects, 1,739 live columns, and 38 parsed view dependencies across four named target datasets.

### 4. Change-safety validation

The private schema package includes explicit checks for prohibited destructive patterns. Examples include unrestricted use of operations such as:

- `CREATE OR REPLACE TABLE`
- `UPDATE`
- `DELETE`
- `TRUNCATE`
- `DROP`
- `MERGE`

The purpose is not to claim that these SQL operations are always wrong. The requirement is that a bounded governed package must not perform them when its approved scope is additive/read-only.

### 5. Downstream-interface validation

Approved semantic or analytical views are checked so that candidate/proposed data does not leak into a controlled consumer interface.

### 6. Repeatability and evidence validation

Where relevant, artifacts can be fingerprinted with SHA-256 and validated against expected manifests or frozen definitions. Re-running a validator should produce the same decision when the controlled inputs have not changed.

## Example UAT-style scenarios

### Scenario A — valid governed package identity

**Given** a package record is eligible for governed use  
**When** identity validation runs  
**Then** the required NDC11 format is valid, the value is unique within the governed set, and the required provenance fields are present.

### Scenario B — ambiguous relationship

**Given** two records have similar product or manufacturer names  
**And** no approved identifier-based relationship exists  
**When** the mapping workflow evaluates them  
**Then** it must not create an approved relationship automatically and must preserve an unresolved/human-review status.

### Scenario C — unsafe schema change

**Given** a change package is approved only for additive schema work  
**When** the validator detects a prohibited destructive SQL pattern  
**Then** validation fails and the package is blocked from that governed execution path.

### Scenario D — approved analytical view

**Given** a consumer uses an approved read-only view  
**When** the view definition is validated  
**Then** only approved fields and relationships are exposed and unresolved/candidate-only content remains outside the approved interface.

## Defect triage model

When a validation check fails, the next question is not simply “how do we make the test green?” The issue is classified first:

```text
Validation failure
      ↓
Is the source wrong or changed?
      ↓ no
Is identity / mapping unresolved?
      ↓ no
Is the requirement or business rule wrong?
      ↓ no
Is the implementation inconsistent with the approved rule?
      ↓
Technical defect
```

This distinction matters because source changes, requirement gaps, data-quality exceptions, and code defects require different owners and resolutions.

## Evidence path

For recruiter review, this public repository provides simplified examples only. The full validators remain private because the implementation repository also contains environment-specific controls and source-governance material that has not been approved for public redistribution.
