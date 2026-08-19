-- Sanitized portfolio example.
-- This is not production SQL and contains no private project identifiers.
-- Purpose: demonstrate the pattern used to expose approved, read-only data
-- while excluding unresolved/candidate records from a consumer-facing view.

CREATE OR REPLACE VIEW portfolio_example.approved_package_evidence_v1 AS
SELECT
  package_identity_id,
  ndc11,
  source_name,
  source_record_date,
  provenance_status
FROM portfolio_example.governed_package_evidence_v1
WHERE approval_status = 'APPROVED'
  AND provenance_status = 'VERIFIED'
  AND ndc11 IS NOT NULL;

-- Example validation query: governed NDC11 values should be unique.
SELECT
  ndc11,
  COUNT(*) AS row_count
FROM portfolio_example.governed_package_evidence_v1
WHERE approval_status = 'APPROVED'
GROUP BY ndc11
HAVING COUNT(*) > 1;

-- Acceptance expectation:
-- the duplicate query returns zero rows for the bounded approved set.
