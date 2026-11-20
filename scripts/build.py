"""Rebuild the whole book from its sources.

  python scripts/build.py                 # figures, bib, TXT->TeX, LuaLaTeX+biber, book.pdf, QA
  python scripts/build.py --experiment    # also re-run the UCI Digits experiment first
  python scripts/build.py --no-qa         # skip the QA report

Steps and their logs go to build_logs/ (git-ignored). Stops at the first failing step.
"""
import shutil, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOGS = ROOT / "build_logs"
PY = sys.executable
TIMEOUT = 300   # seconds per step; a full LuaLaTeX build takes about 20-90 s


def step(name, cmd):
    LOGS.mkdir(exist_ok=True)
    t = time.time()
    try:   # a LaTeX run that loops must not hang the build (IR-19)
        res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
                             errors="replace", timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        print(f"[FAILED] {name}: timed out after {TIMEOUT}s"); sys.exit(124)
    (LOGS / f"{name}.log").write_text(res.stdout + "\n" + res.stderr, encoding="utf-8")
    print(f"[{'ok' if res.returncode == 0 else 'FAILED'}] {name} ({time.time() - t:.0f}s)")
    if res.returncode != 0:
        print(f"    see build_logs/{name}.log"); sys.exit(res.returncode)


def main():
    args = set(sys.argv[1:])
    if "--experiment" in args:
        step("experiment", [PY, "python/generate_chart.py"])
    step("results", [PY, "python/describe_results.py"])
    step("figures", [PY, "python/make_figures.py"])
    step("bibliography", [PY, "scripts/make_bib.py"])
    step("txt2tex", [PY, "-X", "utf8", "scripts/txt2tex.py"])
    step("latex", ["latexmk", "-g", "main.tex"])
    for _ in range(3):   # near-empty chapter-end pages: tighten those chapters and rebuild (IR-15)
        if subprocess.run([PY, "-X", "utf8", "scripts/layout.py"], cwd=ROOT).returncode == 0:
            break
        step("latex", ["latexmk", "-g", "main.tex"])
    shutil.copyfile(ROOT / "main.pdf", ROOT / "book.pdf")
    print("book.pdf updated")
    if "--no-qa" not in args:
        res = subprocess.run([PY, "-X", "utf8", "scripts/qa.py", "super"], cwd=ROOT)
        print("QA report: agents/runs/qa/qa_report.md")
        sys.exit(res.returncode)


if __name__ == "__main__":
    main()
