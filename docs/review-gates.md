# Review Gates

Review gates are deterministic project-state checks. They do not prove that a study is correct. They show whether the current project record is missing information that a researcher should fix before treating it as ready for a claim, handoff, or deliverable.

## What VELA Checks

- whether the project has a research question;
- whether at least one material has been recorded;
- whether at least one candidate claim exists;
- whether evidence has source, access time, verification status, and rights or ethics notes;
- whether supported claims are linked to evidence with a support explanation;
- whether method notes and assumptions are visible;
- whether a Codex handoff is scoped enough for the task;
- whether export should be blocked by privacy or truthfulness risk.

## Gate Rules

- Missing required evidence or method fields: `block`.
- Draft or unresolved items: `revise`.
- Reviewed and sufficient items: `ready` for the specific workflow step only.

A passed method check does not automatically pass evidence, claim, ethics, or writing checks.

## What Checks Do Not Do

VELA does not automatically verify every citation, judge causality, write a paper, certify publication readiness, or decide commercial eligibility. It reports the current workflow state and the next repairable gap.
