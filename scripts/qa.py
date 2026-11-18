"""Deterministic quality checks behind the qa-* skills (.claude/skills/qa-*/SKILL.md).

Usage (from the project root):
  python scripts/qa.py super            # all checks, writes agents/runs/qa/qa_report.md (+ .json)
  python scripts/qa.py bidi|table|code|img|typeset|infra|cls-version
  python scripts/qa.py code --rerun     # also re-runs the experiment into a temp dir and compares
Exit code: 0 = no FAIL, 1 = at least one FAIL. WARN items do not fail the run.
"""
import csv, json, re, subprocess, sys, tempfile, shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / "chapters"
LOG = ROOT / "main.log"
PDF = ROOT / "main.pdf"
MIN_PAGES = 25


class Report:
    def __init__(self, skill):
        self.skill, self.items = skill, []

    def add(self, status, check, detail=""):
        self.items.append({"skill": self.skill, "status": status, "check": check, "detail": detail})

    def ok(self, c, d=""): self.add("PASS", c, d)
    def warn(self, c, d=""): self.add("WARN", c, d)
    def fail(self, c, d=""): self.add("FAIL", c, d)


def txt_units():
    return sorted(p for p in CH.glob("*.txt"))


def body(p):
    return re.split(r"^## מקורות ל", p.read_text(encoding="utf-8"), flags=re.M)[0]


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", **kw)


# ------------------------------------------------------------------ qa-BiDi
def qa_bidi():
    r = Report("qa-BiDi")
    for p in txt_units():
        for n, line in enumerate(body(p).splitlines(), 1):
            if line.count("(") != line.count(")"):
                r.warn("unbalanced parentheses", f"{p.name}:{n}")
            if re.search(r"[\u0590-\u05FF]\([A-Za-z]|[A-Za-z]\)[\u0590-\u05FF]", line):
                r.warn("parenthesis glued between Hebrew and Latin", f"{p.name}:{n}")
    for f in (ROOT / "latex" / "figures").glob("*.tex"):
        t = f.read_text(encoding="utf-8")
        if "\\begin{tikzpicture}" in t and "bookdiagram" not in t:
            r.fail("TikZ figure outside bookdiagram (RTL wrapper)", f.name)
        if re.search(r"node[^;]*\\pardir", t):
            r.fail("\\pardir inside a TikZ node (IR-05)", f.name)
    cls = (ROOT / "latex" / "aibook.cls").read_text(encoding="utf-8")
    if "he/.style={execute at begin node={\\textdir TRT}}" in cls:
        r.ok("node direction rule in class", "he style sets \\textdir only")
    else:
        r.fail("node direction rule in class", "he style changed")
    fams = re.findall(r"\\newfontfamily\\(\w+)\[([^\]]*Script=Hebrew[^\]]*)\]", cls)
    nolig = [f for f, opts in fams if "Ligatures=NoCommon" not in opts]
    (r.ok if fams and not nolig else r.fail)("Hebrew font families without Latin ligatures (IR-10)", ", ".join(nolig) or f"{len(fams)} families")
    raw = [f.name for f in [ROOT / "main.tex", *(ROOT / "latex" / "chapters").glob("*.tex")]
           if "\\begin{tcolorbox}" in f.read_text(encoding="utf-8")]
    (r.ok if not raw else r.fail)("no raw tcolorbox outside the class wrappers (IR-11)", ", ".join(raw))
    base = re.search(r"aibook/base/\.style=\{([^}]*)", cls)
    (r.ok if base and "unbreakable" in base.group(1) else r.fail)("content boxes unbreakable (IR-09)")
    if PDF.exists():
        t = run(["pdftotext", "-enc", "UTF-8", "-f", "9", "-l", "9", str(PDF), "-"]).stdout
        heb = len(re.findall(r"[\u0590-\u05FF]", t))
        (r.ok if heb > 200 else r.fail)("Hebrew text extractable from PDF (page 9)", f"{heb} Hebrew chars")
    return r


# ------------------------------------------------------------------ qa-table
def qa_table():
    r = Report("qa-table")
    for p in txt_units():
        t = body(p)
        ids = re.findall(r"^\[טבלה\s+(\d+)\.(\d+):", t, re.M)
        nums = [int(b) for a, b in ids]
        if nums and nums != list(range(1, len(nums) + 1)):
            r.fail("table numbers in order of appearance", f"{p.name}: {['.'.join(i) for i in ids]}")
        elif nums:
            r.ok("table numbers in order of appearance", f"{p.name}: {len(nums)} tables")
        for m in re.finditer(r"^\[טבלה[^\n]*\]\n(.*?)^\[/טבלה\]", t, re.M | re.S):
            rows = [x for x in m.group(1).splitlines() if x.strip() and not x.startswith("[ממתין")]
            cols = {len(x.split("|")) for x in rows}
            (r.ok if len(cols) == 1 else r.fail)("constant column count", f"{p.name}: {sorted(cols)}")
    # table 5.1 must equal the experiment CSV
    csvp = ROOT / "python" / "data" / "digits_accuracy.csv"
    t5 = (CH / "chapter_05.txt").read_text(encoding="utf-8")
    m = re.search(r"^\[טבלה 5\.\d+: דיוק אימון[^\n]*\]\n(.*?)^\[/טבלה\]", t5, re.M | re.S)
    if m and csvp.exists():
        data = {int(row["epoch"]): row for row in csv.DictReader(csvp.open(encoding="utf-8"))}
        bad, n = [], 0
        for line in m.group(1).splitlines()[1:]:
            cells = [c.strip() for c in line.split("|")]
            if len(cells) != 3 or not cells[0].isdigit():
                bad.append(line[:40]); continue
            e, tr, te = int(cells[0]), float(cells[1]), float(cells[2])
            n += 1
            if abs(tr - float(data[e]["train_accuracy"])) > 5e-4 or abs(te - float(data[e]["test_accuracy"])) > 5e-4:
                bad.append(f"epoch {e}")
        (r.ok if not bad and n else r.fail)("experiment table matches CSV", f"{n} rows; mismatches: {bad}")
    return r


# ------------------------------------------------------------------ qa-code
def qa_code(rerun=False):
    r = Report("qa-code")
    for f in list((ROOT / "python").glob("*.py")) + list((ROOT / "scripts").glob("*.py")):
        res = run([sys.executable, "-m", "py_compile", str(f)])
        (r.ok if res.returncode == 0 else r.fail)("compiles", f.name)
    cfg = json.loads((ROOT / "python" / "experiment_config.json").read_text(encoding="utf-8"))
    (r.ok if isinstance(cfg.get("random_seed"), int) else r.fail)("fixed random seed", str(cfg.get("random_seed")))
    src = (ROOT / "python" / "generate_chart.py").read_text(encoding="utf-8")
    (r.ok if "StandardScaler().fit(X_tr)" in src else r.fail)("scaler fitted on training split only (no leakage)")
    (r.ok if re.search(r"partial_fit\(X_tr_s", src) and "partial_fit(X_te" not in src else r.fail)(
        "model never fitted on the test split")
    s = json.loads((ROOT / "python" / "data" / "digits_summary.json").read_text(encoding="utf-8"))
    rows = list(csv.DictReader((ROOT / "python" / "data" / "digits_accuracy.csv").open(encoding="utf-8")))
    last = rows[-1]
    same = (float(last["test_accuracy"]) == s["final_epoch"]["test_accuracy"] and len(rows) == cfg["epochs"])
    (r.ok if same else r.fail)("summary JSON consistent with CSV", f"{len(rows)} epochs")
    fig = ROOT / "assets" / "charts" / "fig5_1_accuracy.pdf"
    csvp = ROOT / "python" / "data" / "digits_accuracy.csv"
    (r.ok if fig.exists() and fig.stat().st_mtime >= csvp.stat().st_mtime else r.fail)("figure 5.1 newer than its CSV")
    if rerun:
        tmp = Path(tempfile.mkdtemp())
        try:
            shutil.copytree(ROOT / "python", tmp / "python", ignore=shutil.ignore_patterns("data", "__pycache__"))
            (tmp / "assets" / "charts").mkdir(parents=True)
            res = run([sys.executable, "-c", "import sys; sys.path.insert(0,'python'); import generate_chart as g; g.run()"], cwd=tmp)
            new = (tmp / "python" / "data" / "digits_accuracy.csv").read_text(encoding="utf-8")
            (r.ok if new == csvp.read_text(encoding="utf-8") else r.fail)("experiment reproducible (re-run, byte-identical CSV)", res.stderr[-200:])
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    return r


# ------------------------------------------------------------------ qa-img
def qa_img():
    r = Report("qa-img")
    conv = (ROOT / "scripts" / "txt2tex.py").read_text(encoding="utf-8")
    figmap = dict(re.findall(r'"([\dנ]+\.\d+)": \("(?:tikz|pdf)", "([^"]+)"\)', conv))
    for p in txt_units():
        t = body(p)
        ids = re.findall(r"^\[איור\s+([\dנ]+)\.(\d+):", t, re.M)
        nums = [int(b) for a, b in ids]
        if nums != list(range(1, len(nums) + 1)):
            r.fail("figure numbers in order of appearance", f"{p.name}: {ids}")
        for a, b in ids:
            path = figmap.get(f"{a}.{b}")
            (r.ok if path and (ROOT / path).exists() else r.fail)("figure asset exists", f"{a}.{b} -> {path}")
    ext = [f.name for f in (ROOT / "assets" / "images").glob("*") if f.name != ".gitkeep"]
    (r.ok if not ext else r.warn)("no external images", ", ".join(ext) or "assets/images is empty")
    for f in (ROOT / "assets" / "charts").glob("*.pdf"):
        out = run(["pdffonts", str(f)]).stdout
        (r.fail if "Type 3" in out else r.ok)("chart fonts are not Type 3", f.name)
    if PDF.exists():
        out = run(["pdffonts", str(PDF)]).stdout
        notemb = [l for l in out.splitlines()[2:] if l.split() and " no " in l[50:62]]
        (r.ok if not notemb else r.fail)("all PDF fonts embedded", f"{len(notemb)} not embedded")
    return r


# ------------------------------------------------------------------ qa-typeset
def qa_typeset():
    r = Report("qa-typeset")
    if not LOG.exists() or not PDF.exists():
        r.fail("compiled output exists", "main.log / main.pdf missing"); return r
    log = LOG.read_text(encoding="utf-8", errors="replace")
    errs = re.findall(r"^! .*|^\S+:\d+: .*", log, re.M)
    (r.ok if not errs else r.fail)("no LaTeX errors", "; ".join(errs[:3]))
    undef = re.findall(r"(?:Citation|Reference) `([^']+)' .*undefined", log)
    (r.ok if not undef else r.fail)("no undefined references or citations", ", ".join(sorted(set(undef))[:8]))
    (r.ok if "Label(s) may have changed" not in log else r.warn)("labels stable (no rerun needed)")
    miss = sorted(set(re.findall(r"Missing character: There is no (\S+)", log)))
    (r.ok if not miss else r.fail)("no missing glyphs", " ".join(miss))
    over = [float(x) for x in re.findall(r"Overfull \\hbox \(([\d.]+)pt too wide", log)]
    big = [x for x in over if x > 5]
    (r.ok if not big else r.fail)("no text beyond the margins (overfull > 5pt)", f"{len(over)} overfull, {len(big)} > 5pt, max {max(over, default=0):.1f}pt")
    pages = int(re.search(r"Pages:\s+(\d+)", run(["pdfinfo", str(PDF)]).stdout).group(1))
    (r.ok if pages >= MIN_PAGES else r.fail)(f"at least {MIN_PAGES} pages", f"{pages} pages")
    ph = [p.name for p in txt_units() if re.search(r"\[ממתין", body(p))]
    (r.ok if not ph else r.fail)("no placeholders in TXT sources", ", ".join(ph))
    gen = [f.name for f in (ROOT / "latex").rglob("*.tex") if "\\placeholder{" in f.read_text(encoding="utf-8")]
    (r.ok if not gen else r.fail)("no placeholders in generated TeX", ", ".join(gen))
    toc = (ROOT / "main.toc")
    if toc.exists():
        n = len(re.findall(r"\\contentsline \{chapter\}", toc.read_text(encoding="utf-8", errors="replace")))
        (r.ok if n >= 10 else r.fail)("TOC lists abstract, 7 chapters, appendix and references", f"{n} chapter entries")
    for kind, ext in (("figures", "lof"), ("tables", "lot")):
        f = ROOT / f"main.{ext}"
        n = len(re.findall(r"\\contentsline", f.read_text(encoding="utf-8", errors="replace"))) if f.exists() else 0
        (r.ok if n else r.fail)(f"list of {kind} populated", f"{n} entries")
    return r


# ------------------------------------------------------------------ qa-infra
REQUIRED = ["main.tex", "latex/aibook.cls", "references.bib", ".latexmkrc", "scripts/build.py",
            "scripts/txt2tex.py", "scripts/make_bib.py", "scripts/qa.py", "python/generate_chart.py",
            "python/make_figures.py", "python/experiment_config.json", "docs/PRD.md", "docs/PLAN.md",
            "docs/TODO.md", "docs/STATUS.md", "docs/INCIDENTS.md", "requirements.txt"]


def qa_infra():
    r = Report("qa-infra")
    for f in REQUIRED:
        (r.ok if (ROOT / f).exists() else r.fail)("required file", f)
    for p in txt_units():
        if p.stem == "abstract":
            continue
        tex = ROOT / "latex" / "chapters" / f"{p.stem}.tex"
        (r.ok if tex.exists() and tex.stat().st_mtime >= p.stat().st_mtime else r.fail)(
            "generated TeX up to date with its TXT", tex.name)
    bib = (ROOT / "references.bib").read_text(encoding="utf-8")
    keys = set(re.findall(r"@\w+\{(S-ch\d\d-\d\d),", bib))
    cited = set()
    for p in txt_units():
        cited |= set(re.findall(r"S-ch\d\d-\d\d", body(p)))
    missing = sorted(cited - keys)
    (r.ok if not missing else r.fail)("every cited source has a bib entry", ", ".join(missing))
    main = (ROOT / "main.tex").read_text(encoding="utf-8")
    for need in ("\\tableofcontents", "\\listoffigures", "\\listoftables", "\\printbibliography", "\\makecover"):
        (r.ok if need in main else r.fail)("main.tex element", need)
    (r.ok if "pdf_mode = 4" in (ROOT / ".latexmkrc").read_text() else r.fail)("latexmk uses LuaLaTeX")
    return r


# ------------------------------------------------------------------ qa-cls-version
def qa_cls_version():
    r = Report("qa-cls-version")
    cls = (ROOT / "latex" / "aibook.cls").read_text(encoding="utf-8")
    pv = re.search(r"\\ProvidesClass\{aibook\}\[(\d{4})/(\d\d)/(\d\d) v([\d.]+)", cls)
    iv = re.search(r"\\def\\aibook@version\{([\d.]+)\}", cls)
    cl = re.findall(r"^%\s+(\d+\.\d+\.\d+) \((\d{4}-\d\d-\d\d)\)", cls, re.M)
    if not (pv and iv and cl):
        r.fail("version fields present"); return r
    (r.ok if pv[4] == iv[1] == cl[-1][0] else r.fail)("ProvidesClass = \\aibook@version = latest CHANGELOG", f"{pv[4]} / {iv[1]} / {cl[-1][0]}")
    (r.ok if f"{pv[1]}-{pv[2]}-{pv[3]}" == cl[-1][1] else r.fail)("ProvidesClass date = latest CHANGELOG date")
    if LOG.exists():
        log = LOG.read_text(encoding="utf-8", errors="replace")
        (r.ok if f"v{pv[4]}" in log else r.fail)("compiled with this class version", f"v{pv[4]} in main.log")
    return r


SKILLS = {"bidi": qa_bidi, "table": qa_table, "code": qa_code, "img": qa_img,
          "typeset": qa_typeset, "infra": qa_infra, "cls-version": qa_cls_version}


def write_report(items):
    out = ROOT / "agents" / "runs" / "qa"
    out.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    counts = {s: sum(1 for i in items if i["status"] == s) for s in ("PASS", "WARN", "FAIL")}
    lines = [f"# דוח qa-super ({stamp})", "", "> נוצר על ידי `python scripts/qa.py super`. כל שורה היא בדיקה דטרמיניסטית.", "",
             f"**PASS {counts['PASS']} · WARN {counts['WARN']} · FAIL {counts['FAIL']}**", "",
             "| Skill | מצב | בדיקה | פירוט |", "|---|---|---|---|"]
    for i in items:
        lines.append(f"| {i['skill']} | {i['status']} | {i['check']} | {i['detail'].replace('|', '/')} |")
    (out / "qa_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out / "qa_report.json").write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
    return counts


def main():
    args = sys.argv[1:] or ["super"]
    which, rerun = args[0], "--rerun" in args
    names = list(SKILLS) if which == "super" else [which]
    items = []
    for n in names:
        rep = SKILLS[n](rerun) if n == "code" else SKILLS[n]()
        items += rep.items
    counts = write_report(items) if which == "super" else None
    for i in items:
        if i["status"] != "PASS":
            print(f"{i['status']:4} {i['skill']:15} {i['check']} :: {i['detail']}")
    tot = {s: sum(1 for i in items if i["status"] == s) for s in ("PASS", "WARN", "FAIL")}
    print(f"qa {which}: PASS {tot['PASS']} WARN {tot['WARN']} FAIL {tot['FAIL']}")
    return 1 if tot["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main())
