---
name: qa-typeset
description: Check the compiled book: LaTeX errors, undefined references/citations, missing glyphs, text beyond margins, page count, placeholders, TOC and lists of figures/tables.
---

# qa-typeset: עימוד והידור

**פקודה:** `python -X utf8 scripts/qa.py typeset` (אחרי `python scripts/build.py`).

## בדיקות (FAIL אם נכשלות)
1. אין שגיאות LaTeX ב-`main.log`.
2. אין הפניות או ציטוטים לא מוגדרים.
3. אין "Missing character". תו שחסר בגופן Assistant ממופה במתמטיקה ב-`esc()` של `scripts/txt2tex.py`, ולא מתוקן ידנית.
4. אין חריגה מהשוליים: Overfull גדול מ-5pt.
5. לפחות 25 עמודים (`pdfinfo`).
6. אין סימוני `[ממתין` ב-TXT, ואין `\placeholder` בקובצי TeX שנוצרו.
7. תוכן העניינים כולל לפחות 10 רשומות פרק, ורשימת האיורים ורשימת הטבלאות אינן ריקות.
