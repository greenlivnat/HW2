---
name: qa-BiDi
description: Check Hebrew/English directionality: parentheses, mixed runs, the RTL rules for TikZ nodes and boxes, and that Hebrew text is extractable from the PDF.
---

# qa-BiDi: כיווניות עברית ואנגלית

**פקודה:** `python -X utf8 scripts/qa.py bidi`

## בדיקות אוטומטיות
1. סוגריים מאוזנים בכל שורה של `chapters/*.txt` (WARN).
2. סוגר שנצמד בין אות עברית לאות לטינית, כמו `מילה(ML` (WARN): סימן לשבירת כיווניות.
3. כל איור TikZ ב-`latex/figures/` עטוף ב-`bookdiagram`, ואין `\pardir` בתוך צומת (FAIL). זה הכלל שנלמד מ-IR-05.
4. הסגנון `he` במחלקה מגדיר רק `\textdir TRT` (FAIL אם שונה).
5. ב-PDF יש טקסט עברי שניתן לחלץ (`pdftotext -enc UTF-8`). FAIL אם אין.

## בדיקה ידנית (Detector)
עמוד עם מונחים באנגלית בסוגריים, עמוד עם ציטוטי IEEE כמו [12], ועמוד עם נוסחה: סדר המילים, הסוגריים והמספרים נכון מימין לשמאל.
