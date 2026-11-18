---
name: qa-code
description: Check the Python code and the UCI Digits experiment: compiles, fixed seed, no train/test leakage, outputs consistent, optional byte-identical re-run.
---

# qa-code: קוד וניסוי

**פקודה:** `python -X utf8 scripts/qa.py code` (ועם `--rerun` לבדיקת שחזור מלאה, כ-15 שניות).

## בדיקות
1. כל קובצי `python/*.py` ו-`scripts/*.py` עוברים קומפילציה.
2. `random_seed` קבוע ב-`python/experiment_config.json`.
3. מניעת זליגה: ה-`StandardScaler` מותאם רק לקבוצת האימון, והמודל לא מאומן על קבוצת הבדיקה.
4. `digits_summary.json` תואם ל-CSV (מספר תקופות, ערך אחרון).
5. איור 5.1 חדש יותר מה-CSV שלו.
6. `--rerun`: הרצה בתיקייה זמנית נותנת CSV זהה בית אחר בית.

## כלל יושר
אסור לשנות את `experiment_config.json` כדי לקבל צורת גרף רצויה (PRD §5). שינוי מחייב רשומה ב-`docs/PROMPT_HISTORY.md` ונימוק.
