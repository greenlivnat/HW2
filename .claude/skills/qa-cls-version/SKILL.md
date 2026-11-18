---
name: qa-cls-version
description: Check that the custom class version is consistent: ProvidesClass, \aibook@version and the latest CHANGELOG entry agree, and the compiled log used that version.
---

# qa-cls-version: גרסת התבנית

**פקודה:** `python -X utf8 scripts/qa.py cls-version`

## בדיקות
1. ‏`\ProvidesClass{aibook}[YYYY/MM/DD vX.Y.Z]`, ‏`\def\aibook@version{X.Y.Z}` והרשומה האחרונה ב-CHANGELOG שבראש `latex/aibook.cls` זהים.
2. תאריך ה-ProvidesClass שווה לתאריך הרשומה האחרונה.
3. `main.log` מראה שההידור השתמש בגרסה הזו.

## נוהל שינוי בתבנית
כל שינוי ב-CLS: מעלים גרסה (תיקון: ‏Z, תכונה: ‏Y), מוסיפים שורת CHANGELOG, בונים מחדש ומריצים qa-super.
