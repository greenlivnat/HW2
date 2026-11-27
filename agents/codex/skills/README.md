# Codex skill manifests

These portable SKILL.md manifests are stored here because the execution profile declares the repository .agents path read-only. Codex discovers repo-local Skills under .agents/skills. The review and Fixer assignments were issued directly before these manifests were authored. Automatic Skills discovery and invocation were not verified.

| Codex Skill | Related existing Claude workflow |
|---|---|
| academic-review | agent-research, agent-writer |
| latex-publication-review | qa-bidi, qa-typeset, qa-img, qa-table |
| experiment-reproducibility | qa-code |
| detector-red-team | qa-super, qa-typeset |
| targeted-fixer | writer and repair workflow, qa-infra |
| collaboration-evidence | prompt and status tracking |

## Evidence and acceptance

| Skill | Inputs | Expected output and acceptance |
|---|---|---|
| Academic review | Chapter sources, bibliography, primary studies | Issues linked to the primary passage, with correct units, population and claim scope |
| LaTeX publication review | Generated TeX, page renders, typography QA | Page-specific notes and actual comparison renders for any proposed visible fix |
| Experiment reproducibility | Fixed configuration, stored CSV and summary, isolated environment | Versioned rerun and honest comparison against stored values |
| Detector red team | Baseline, proposed diff, tests and rendered artifacts where available | Independent per-issue verdict and explicit limits |
| Targeted fixer | Confirmed issues and acceptance criteria | Scoped source proposal, generated counterparts and targeted test evidence |
| Collaboration evidence | Git status, recorded manual actions and contribution history | Verified branch, attribution and actual publication status, with pending operations marked |

The activity records in [the independent review](../../../docs/CODEX_REVIEW.md) document equivalent steps assigned directly to actual roles. The six manifests are preserved as portable workflow documentation. Manual application of the manifests themselves, automatic discovery and invocation remain unverified.
