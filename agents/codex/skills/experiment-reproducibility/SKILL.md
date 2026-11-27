---
name: experiment-reproducibility
description: Review the fixed UCI Digits experiment and its reports.
---

# experiment-reproducibility

Read experiment_config.json, generate_chart.py, stored CSV and summary. Compare split and scaler inputs, metadata and rounded derived metrics. Use scripts/qa.py code --rerun in an isolated environment. Record versions and mismatches. Preserve original outputs if reproduction fails.
