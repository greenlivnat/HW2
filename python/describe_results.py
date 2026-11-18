"""Compute shape facts of the accuracy curves from the CSV (no eyeballing, see docs/INCIDENTS.md IR-12).
Writes python/data/digits_shape.json. Run from the project root: python python/describe_results.py"""
import csv, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
rows = list(csv.DictReader((ROOT / "python" / "data" / "digits_accuracy.csv").open(encoding="utf-8")))
ep = [int(r["epoch"]) for r in rows]
tr = [float(r["train_accuracy"]) for r in rows]
te = [float(r["test_accuracy"]) for r in rows]
gaps = [a - b for a, b in zip(tr, te)]
k = max(range(len(gaps)), key=lambda i: (gaps[i], -i))
facts = {
    "test_declines": [{"epoch": ep[i], "from": te[i - 1], "to": te[i]} for i in range(1, len(te)) if te[i] < te[i - 1]],
    "train_declines": [{"epoch": ep[i], "from": tr[i - 1], "to": tr[i]} for i in range(1, len(tr)) if tr[i] < tr[i - 1]],
    "max_gap": {"epoch": ep[k], "train": tr[k], "test": te[k], "gap": round(gaps[k], 4)},
    "final": {"epoch": ep[-1], "train": tr[-1], "test": te[-1], "gap": round(gaps[-1], 4)},
    "best_test": {"epoch": ep[max(range(len(te)), key=lambda i: (te[i], -i))], "test": max(te)},
    "test_range_from_epoch_30": [min(te[29:]), max(te[29:])],
}
(ROOT / "python" / "data" / "digits_shape.json").write_text(json.dumps(facts, indent=2), encoding="utf-8")
print(json.dumps(facts))
