# Proposed and source-verified improvements

These changes were independently verified at source level and are **not incorporated into the submitted publication**. The [actual Git patch](proposed-publication-corrections.patch) captures the five authoritative chapter files, five generated counterparts, converter and QA changes. The [archived focused test](test_codex_regressions.py.txt) was an untracked Python file and is preserved verbatim as evidence.

- Baseline: `0d5a0ad11e1b3216792b98892ee0f163cf390c1c`.
- Patch SHA-256: `4967eece6f194f53f8cfff66405351bd3a6b972c1efb12c3a5c28fe82c29468f`.
- Test SHA-256: `b96c8078e2e31af4c4efe30df3614902512f7a4f422812ee8dd3752209dfdb55`.

Git verified the reverse patch before the narrow restoration and verified forward applicability after restoration. Restoration was confined to the twelve known modified files. The original PDF matches the baseline Git object byte-for-byte.

To take these proposals forward in a separate working branch based on the verified baseline, first run `git apply --check --unidiff-zero docs/review-evidence/proposed-publication-corrections.patch`, then apply with the same flag and without `--check`. Copy the archived test to `scripts/test_codex_regressions.py` in that branch only. Rebuild the book, rerun QA and obtain an independent printed-page review before considering publication.
