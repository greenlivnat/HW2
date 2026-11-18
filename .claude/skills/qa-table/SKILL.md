---
name: qa-table
description: Check the book's tables: numbering in order of appearance, constant column count, and that the experiment table equals the CSV produced by the experiment.
---

# qa-table: טבלאות

**פקודה:** `python -X utf8 scripts/qa.py table`

## בדיקות
1. מספרי הטבלאות בכל פרק עולים לפי סדר ההופעה (5.1 לפני 5.2). FAIL אחרת.
2. בכל טבלה אותו מספר עמודות בכל שורה.
3. טבלת הניסוי בפרק 5 זהה ל-`python/data/digits_accuracy.csv` (סטייה של 0.0005 לכל היותר, כלומר עיגול לשלוש ספרות). FAIL אם יש שורה שלא תואמת.

## עיצוב (CLS)
שורת כותרת על Midnight Blue, קווי booktabs ב-Turquoise, כיתוב מעל הטבלה. טבלה מספרית בעמודות ממורכזות, וטבלת טקסט ב-`tabularx` ברוחב השורה.
