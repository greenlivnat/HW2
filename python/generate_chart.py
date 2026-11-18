"""M4 experiment: train/test accuracy per epoch on UCI Digits (sklearn load_digits).

Reads python/experiment_config.json, writes python/data/digits_accuracy.csv,
python/data/digits_summary.json and assets/charts/fig5_1_accuracy.pdf.
Run from the project root:  python python/generate_chart.py
"""
import csv, json, platform, warnings
from pathlib import Path

import numpy as np
import sklearn
from sklearn.datasets import load_digits
from sklearn.exceptions import ConvergenceWarning
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "python" / "experiment_config.json").read_text(encoding="utf-8"))
DATA = ROOT / "python" / "data"
CSV_PATH = DATA / "digits_accuracy.csv"
SUMMARY_PATH = DATA / "digits_summary.json"


def run():
    X, y = load_digits(return_X_y=True)
    seed = CFG["random_seed"]
    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=CFG["test_size"], random_state=seed,
        stratify=y if CFG["stratify"] else None)
    # Leakage guard: the scaler sees the training split only.
    scaler = StandardScaler().fit(X_tr)
    X_tr_s, X_te_s = scaler.transform(X_tr), scaler.transform(X_te)
    # Information only: identical pixel vectors that appear in both splits (not removed, reported).
    dup_across = len({r.tobytes() for r in X_tr.astype(np.int8)} & {r.tobytes() for r in X_te.astype(np.int8)})

    clf = MLPClassifier(hidden_layer_sizes=tuple(CFG["hidden_layer_sizes"]),
                        activation=CFG["activation"], solver=CFG["solver"],
                        learning_rate_init=CFG["learning_rate_init"], alpha=CFG["alpha"],
                        batch_size=CFG["batch_size"], random_state=seed, shuffle=True)
    classes = np.unique(y)
    rows = []
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", ConvergenceWarning)
        for epoch in range(1, CFG["epochs"] + 1):
            clf.partial_fit(X_tr_s, y_tr, classes=classes)
            rows.append({"epoch": epoch,
                         "train_accuracy": round(float(clf.score(X_tr_s, y_tr)), 4),
                         "test_accuracy": round(float(clf.score(X_te_s, y_te)), 4),
                         "train_loss": round(float(clf.loss_), 4)})
    DATA.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
    last = rows[-1]
    best = max(rows, key=lambda r: (r["test_accuracy"], -r["epoch"]))
    gaps = [r["train_accuracy"] - r["test_accuracy"] for r in rows]
    summary = {
        "n_samples": int(len(y)), "n_train": int(len(y_tr)), "n_test": int(len(y_te)),
        "n_features": int(X.shape[1]), "identical_images_across_splits": int(dup_across), "n_classes": int(len(classes)),
        "final_epoch": last, "max_test_accuracy": best,
        "final_gap": round(last["train_accuracy"] - last["test_accuracy"], 4),
        "max_gap": round(max(gaps), 4),
        "versions": {"python": platform.python_version(), "scikit-learn": sklearn.__version__,
                     "numpy": np.__version__},
        "config": CFG,
    }
    SUMMARY_PATH.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return rows, summary


if __name__ == "__main__":
    rows, s = run()
    from make_figures import fig5_1
    fig5_1(rows)
    print(json.dumps({k: s[k] for k in ("n_train", "n_test", "final_epoch", "max_test_accuracy", "final_gap", "max_gap")}, ensure_ascii=False))
