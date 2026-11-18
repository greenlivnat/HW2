---
name: qa-img
description: Check every figure: asset exists for each [איור] marker, numbering order, no external images, no Type 3 fonts in charts, all PDF fonts embedded.
---

# qa-img: איורים וגרפים

**פקודה:** `python -X utf8 scripts/qa.py img`

## בדיקות
1. לכל סימון `[איור X.Y]` ב-TXT יש קובץ ב-`FIGURES` של `scripts/txt2tex.py`, והקובץ קיים.
2. מספרי האיורים עולים לפי סדר ההופעה.
3. אין תמונות חיצוניות ב-`assets/images/` (WARN אם יש).
4. גרפי Matplotlib בלי גופני Type 3 (`pdf.fonttype=42`).
5. כל הגופנים ב-PDF מוטמעים.

## בדיקה ידנית
פלטה (STYLE_GUIDE §6), Gold רק כסימון ולא כטקסט, תוויות עבריות בגרפים בסדר נכון (הפונקציה `he()` ב-`python/make_figures.py`), ותרשים 4.2 עם 9 בלוקים וחץ לולאה.
