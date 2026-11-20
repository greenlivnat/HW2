# דוח qa-super (2026-11-20 14:49)

> נוצר על ידי `python scripts/qa.py super`. כל שורה היא בדיקה דטרמיניסטית.

**PASS 92 · WARN 0 · FAIL 0**

| Skill | מצב | בדיקה | פירוט |
|---|---|---|---|
| qa-BiDi | PASS | node direction rule in class | he style sets \textdir only |
| qa-BiDi | PASS | Hebrew font families without Latin ligatures (IR-10) | 5 families |
| qa-BiDi | PASS | no raw tcolorbox outside the class wrappers (IR-11) |  |
| qa-BiDi | PASS | content boxes unbreakable (IR-09) |  |
| qa-BiDi | PASS | no breakable content boxes (IR-09, IR-15) | none |
| qa-BiDi | PASS | Hebrew text extractable from PDF (page 9) | 2507 Hebrew chars |
| qa-table | PASS | table numbers in order of appearance | chapter_05.txt: 2 tables |
| qa-table | PASS | constant column count | chapter_05.txt: [4] |
| qa-table | PASS | constant column count | chapter_05.txt: [3] |
| qa-table | PASS | experiment table matches CSV | 10 rows; mismatches: [] |
| qa-code | PASS | compiles | describe_results.py |
| qa-code | PASS | compiles | generate_chart.py |
| qa-code | PASS | compiles | make_figures.py |
| qa-code | PASS | compiles | build.py |
| qa-code | PASS | compiles | layout.py |
| qa-code | PASS | compiles | make_bib.py |
| qa-code | PASS | compiles | qa.py |
| qa-code | PASS | compiles | screenshots.py |
| qa-code | PASS | compiles | txt2tex.py |
| qa-code | PASS | fixed random seed | 42 |
| qa-code | PASS | scaler fitted on training split only (no leakage) |  |
| qa-code | PASS | model never fitted on the test split |  |
| qa-code | PASS | summary JSON consistent with CSV | 40 epochs |
| qa-code | PASS | figure 5.1 newer than its CSV |  |
| qa-code | PASS | experiment reproducible (re-run, byte-identical CSV) |  |
| qa-img | PASS | figure asset exists | נ.1 -> latex/figures/figA_1.tex |
| qa-img | PASS | figure asset exists | נ.2 -> assets/charts/figA_2_scores.pdf |
| qa-img | PASS | figure asset exists | 1.1 -> latex/figures/fig1_1.tex |
| qa-img | PASS | figure asset exists | 2.1 -> latex/figures/fig2_1.tex |
| qa-img | PASS | figure asset exists | 3.1 -> assets/charts/fig3_1_activations.pdf |
| qa-img | PASS | figure asset exists | 3.2 -> latex/figures/fig3_2.tex |
| qa-img | PASS | figure asset exists | 4.1 -> assets/charts/fig4_1_temperature.pdf |
| qa-img | PASS | figure asset exists | 4.2 -> latex/figures/fig4_2.tex |
| qa-img | PASS | figure asset exists | 5.1 -> assets/charts/fig5_1_accuracy.pdf |
| qa-img | PASS | figure asset exists | 6.1 -> latex/figures/fig6_1.tex |
| qa-img | PASS | figure asset exists | 7.1 -> latex/figures/fig7_1.tex |
| qa-img | PASS | chart Hebrew in correct order (IR-14) | matplotlib bidi=yes, he() reverses=no |
| qa-img | PASS | no external images | assets/images is empty |
| qa-img | PASS | chart fonts are not Type 3 | fig3_1_activations.pdf |
| qa-img | PASS | chart fonts are not Type 3 | fig4_1_temperature.pdf |
| qa-img | PASS | chart fonts are not Type 3 | fig5_1_accuracy.pdf |
| qa-img | PASS | chart fonts are not Type 3 | figA_2_scores.pdf |
| qa-img | PASS | all PDF fonts embedded | 0 not embedded |
| qa-typeset | PASS | no LaTeX errors |  |
| qa-typeset | PASS | no undefined references or citations |  |
| qa-typeset | PASS | labels stable (no rerun needed) |  |
| qa-typeset | PASS | no missing glyphs |  |
| qa-typeset | PASS | no text beyond the margins (overfull > 5pt) | 0 overfull, 0 > 5pt, max 0.0pt |
| qa-typeset | PASS | PDF author metadata set | ליאת קפהזידר ולבנת בנסון |
| qa-typeset | PASS | printed page numbers equal PDF page numbers | 43 pages |
| qa-typeset | PASS | no raw TeX markup in the PDF text |  |
| qa-typeset | PASS | at least 25 pages | 43 pages |
| qa-typeset | PASS | no placeholders in TXT sources |  |
| qa-typeset | PASS | no placeholders in generated TeX |  |
| qa-typeset | PASS | TOC lists abstract, 7 chapters, appendix and references | 10 chapter entries |
| qa-typeset | PASS | list of figures populated | 11 entries |
| qa-typeset | PASS | list of tables populated | 2 entries |
| qa-infra | PASS | required file | main.tex |
| qa-infra | PASS | required file | latex/aibook.cls |
| qa-infra | PASS | required file | references.bib |
| qa-infra | PASS | required file | .latexmkrc |
| qa-infra | PASS | required file | scripts/build.py |
| qa-infra | PASS | required file | scripts/txt2tex.py |
| qa-infra | PASS | required file | scripts/make_bib.py |
| qa-infra | PASS | required file | scripts/qa.py |
| qa-infra | PASS | required file | python/generate_chart.py |
| qa-infra | PASS | required file | python/make_figures.py |
| qa-infra | PASS | required file | python/experiment_config.json |
| qa-infra | PASS | required file | docs/PRD.md |
| qa-infra | PASS | required file | docs/PLAN.md |
| qa-infra | PASS | required file | docs/TODO.md |
| qa-infra | PASS | required file | docs/STATUS.md |
| qa-infra | PASS | required file | docs/INCIDENTS.md |
| qa-infra | PASS | required file | requirements.txt |
| qa-infra | PASS | generated TeX up to date with its TXT | appendix.tex |
| qa-infra | PASS | generated TeX up to date with its TXT | chapter_01.tex |
| qa-infra | PASS | generated TeX up to date with its TXT | chapter_02.tex |
| qa-infra | PASS | generated TeX up to date with its TXT | chapter_03.tex |
| qa-infra | PASS | generated TeX up to date with its TXT | chapter_04.tex |
| qa-infra | PASS | generated TeX up to date with its TXT | chapter_05.tex |
| qa-infra | PASS | generated TeX up to date with its TXT | chapter_06.tex |
| qa-infra | PASS | generated TeX up to date with its TXT | chapter_07.tex |
| qa-infra | PASS | every cited source has a bib entry |  |
| qa-infra | PASS | main.tex element | \tableofcontents |
| qa-infra | PASS | main.tex element | \listoffigures |
| qa-infra | PASS | main.tex element | \listoftables |
| qa-infra | PASS | main.tex element | \printbibliography |
| qa-infra | PASS | main.tex element | \makecover |
| qa-infra | PASS | latexmk uses LuaLaTeX |  |
| qa-cls-version | PASS | ProvidesClass = \aibook@version = latest CHANGELOG | 1.2.0 / 1.2.0 / 1.2.0 |
| qa-cls-version | PASS | ProvidesClass date = latest CHANGELOG date |  |
| qa-cls-version | PASS | compiled with this class version | v1.2.0 in main.log |
