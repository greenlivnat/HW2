# Manual publication handoff

Run this from PowerShell with normal repository write access. The sequence stops if origin/main differs from the baseline. Inspect and reconcile any upstream changes before revalidating, committing, and publishing. Never force-push. It also stops if the index is already staged or if the staged paths differ from the reviewed list.

```powershell
Set-Location -LiteralPath 'D:\HW2'
$branch = 'liat/assignment02-critical-review'
$baseline = '0d5a0ad11e1b3216792b98892ee0f163cf390c1c'
$origin = 'https://github.com/greenlivnat/HW2.git'
if ((git branch --show-current) -ne $branch) { throw 'Unexpected branch' }
if ((git config user.name) -ne 'Liat Kafezider') { throw 'Unexpected author' }
if (-not (git config user.email)) { throw 'Missing author email' }
if ((git remote get-url origin) -ne $origin -or (git remote get-url --push origin) -ne $origin) { throw 'Unexpected origin' }
if ((git rev-parse HEAD) -ne $baseline) { throw 'Unexpected HEAD' }
if (Test-Path -LiteralPath '.git/index.lock') { throw 'Index lock present. Investigate the owning process.' }
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) { throw 'Index already staged or unreadable' }
git fetch origin
if ($LASTEXITCODE -ne 0) { throw 'Fetch failed' }
if ((git rev-parse origin/main) -ne $baseline) { throw 'Upstream has changed. Inspect before integrating.' }
git diff --quiet $baseline -- book.pdf chapters latex main.tex references.bib python assets releases scripts
if ($LASTEXITCODE -ne 0) { throw 'Publication paths changed' }
$expectedHash = 'E3C2B9B18AF70B8937621CD21658819F2D6A13E32F36282ABD63EDE6F9951DFC'
if ((Get-FileHash -LiteralPath 'book.pdf').Hash -ne $expectedHash) { throw 'PDF checksum mismatch' }
$paths = @(
    'CHANGELOG.md'
    'COLLABORATION.md'
    'README.md'
    'agents/codex/skills/README.md'
    'agents/codex/skills/academic-review/SKILL.md'
    'agents/codex/skills/collaboration-evidence/SKILL.md'
    'agents/codex/skills/detector-red-team/SKILL.md'
    'agents/codex/skills/experiment-reproducibility/SKILL.md'
    'agents/codex/skills/latex-publication-review/SKILL.md'
    'agents/codex/skills/targeted-fixer/SKILL.md'
    'docs/CODEX_CONTINUATION_STATUS.md'
    'docs/CODEX_EXECUTION_STATUS.md'
    'docs/CODEX_REVIEW.md'
    'docs/INCIDENTS.md'
    'docs/PRD.md'
    'docs/PROMPT_HISTORY.md'
    'docs/PULL_REQUEST.md'
    'docs/STATUS.md'
    'docs/review-evidence/PUBLISH.md'
    'docs/review-evidence/README.md'
    'docs/review-evidence/proposed-publication-corrections.patch'
    'docs/review-evidence/test_codex_regressions.py.txt'
    'prompts/15_codex_recovery.txt'
    'prompts/15a_codex_initial_assignment.txt'
    'prompts/15b_codex_continue_assignment.txt'
    'prompts/15c_codex_environment_recovery.txt'
    'prompts/15d_codex_diagnostic.txt'
    'prompts/16_codex_final_build.txt'
    'prompts/16_codex_final_build_summary.txt'
    'prompts/17_codex_documentation_publication.txt'
)
git add -- @paths
if ($LASTEXITCODE -ne 0) { throw 'Staging failed' }
$staged = @(git diff --cached --name-only)
if ($LASTEXITCODE -ne 0 -or (Compare-Object ($paths | Sort-Object) ($staged | Sort-Object))) { throw 'Unexpected staged paths' }
git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw 'Staged diff validation failed' }
git diff --cached --stat
git diff --cached --name-status
git commit -m 'Document independent Codex review and preserve verified proposals'
if ($LASTEXITCODE -ne 0) { throw 'Commit failed' }
git log -1 --format='%H %an'
git diff --quiet $baseline HEAD -- book.pdf chapters latex main.tex references.bib python assets releases scripts
if ($LASTEXITCODE -ne 0) { throw 'Committed publication files differ' }
git push -u origin $branch
if ($LASTEXITCODE -ne 0) { throw 'Push failed. Preserve the local commit.' }
$remote = git ls-remote --exit-code origin "refs/heads/$branch"
if ($LASTEXITCODE -ne 0 -or ($remote -split '\s+')[0] -ne (git rev-parse HEAD)) { throw 'Remote verification failed' }
```

Use the [complete PR description and browser instructions](../PULL_REQUEST.md). The following commands are for later, **only after Livnat actually merges** and the working tree is safe to switch.

```powershell
cd D:\HW2
git status
git switch main
git rev-parse HEAD
git pull --ff-only origin main
git rev-parse HEAD
git status
```

Record the real output, date, PR and merge reference, changed files and final status in the collaboration log.
