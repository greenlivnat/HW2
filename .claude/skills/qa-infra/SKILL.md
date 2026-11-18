---
name: qa-infra
description: Check the repository infrastructure: required files, generated TeX newer than its TXT, every cited source in references.bib, main.tex elements, LuaLaTeX in latexmk.
---

# qa-infra: תשתית הריפו

**פקודה:** `python -X utf8 scripts/qa.py infra`

## בדיקות
1. קיימים: `main.tex`, ‏`latex/aibook.cls`, ‏`references.bib`, ‏`.latexmkrc`, סקריפטי הבנייה וה-QA, ‏PRD, ‏PLAN, ‏TODO, ‏STATUS, ‏INCIDENTS.
2. כל `latex/chapters/*.tex` חדש יותר מה-TXT שלו (אחרת להריץ `scripts/txt2tex.py`).
3. כל מזהה `S-chXX-NN` שמצוטט בגוף הפרקים קיים ב-`references.bib`.
4. ב-`main.tex` יש שער, תוכן עניינים, רשימת איורים, רשימת טבלאות וביבליוגרפיה.
5. ‏`.latexmkrc` מגדיר LuaLaTeX (`$pdf_mode = 4`).

## בדיקה ידנית
`git status`: כל סוכן כתב רק בתחום שהוקצה לו.
