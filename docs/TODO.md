# TODO

> **עודכן:** 2026-11-20. מסומן ✅ רק מה שנבדק בפועל.

## M4 + M5A
- [x] ניסוי UCI Digits: הגדרות נקבעו מראש (`python/experiment_config.json`), seed 42, ‏Scaler רק על קבוצת האימון, תוצאות ב-`python/data/`
- [x] איורי Matplotlib 3.1, 4.1 ו-5.1 (`python/make_figures.py`), כולל התיקון של R-ch04-10 ("כל השאר" כ-15 טוקנים)
- [x] איורי TikZ 1.1, 2.1, 3.2, 4.2 (9 בלוקים), 6.1, 7.1 ונ.1 (`latex/figures/`)
- [x] ‏`latex/aibook.cls` v1.0.0, ‏`main.tex`, ‏`.latexmkrc` (LuaLaTeX ו-biber)
- [x] ‏`scripts/txt2tex.py` (TXT ← TeX), ‏`scripts/make_bib.py` (IEEE), ‏`scripts/build.py`, ‏`scripts/qa.py`
- [x] ‏Skills: ‏qa-super, ‏qa-BiDi, ‏qa-table, ‏qa-code, ‏qa-img, ‏qa-typeset, ‏qa-infra, ‏qa-cls-version, וחמישה Skills לסוכנים
- [x] ‏Fixer Agent, ומצב Detector ל-Reviewer
- [x] ‏PRD 1.5, ביקורת ועדת מומחים, ‏PLAN, ‏INCIDENTS
- [x] writer: ארבעת המקומות בפרק 5, ‏`chapters/abstract.txt` ועדכון הנספח
- [x] Detector r1 על הספר המהודר
- [x] Fixer: ‏19 הליקויים הקלים מ-M3 וממצאי Detector
- [x] Detector r2 (בדיקה חוזרת)
- [x] ‏STATUS, ‏PROMPT_HISTORY (רשומה 010) ו-commit מקומי

## M5B ו-M6 (אחרי אישור המשתמשת)
- [x] R-ch03-11: עוגן מקור ל-tanh (S-ch03-01 עודכן, ‏S-ch03-05 חדש; `agents/runs/research_m5b_r1.md`)
- [x] D-m5a-08: רווח לבן סביב איור 5.1 וטבלה 5.2 (עמודי איורים נדחסים לראש העמוד, CLS 1.2.0)
- [x] ‏`python scripts/qa.py super --rerun`: ‏92/0/0; הניסוי שוחזר זהה בית אחר בית; הספר נבנה מחדש אחרי ניקוי מלא והטקסט זהה
- [x] משוב: ביקורת חיצונית ב-ChatGPT (`prompts/12_m5b_m6_external_review.txt`), כל ההערות טופלו
- [x] README עם 7 צילומי מסך (`scripts/screenshots.py`), הוראות שחזור, ‏CHANGELOG.md, תגיות v0.1, v0.2, v0.9, v0.95
- [x] Detector ‏M5B ‏(93, ‏REVISE) ← Fixer ← אימות אוטומטי; הנספח עודכן (D13)
- [ ] ליקויים ידועים, קלים ולא חוסמים: D-m5b-03 (נוסחאות ארוכות נשברות בפסקת RTL), ‏D-m5b-06 (URL ברשומה [60] ומילים עבריות ברשומות באנגלית)
- [ ] חבילת התיעוד החיצונית של ChatGPT: ל-`docs/external/` (מקום שמור ב-README §11)
- [ ] v1.0 ו-M7 (‏push), רק באישור מפורש של המשתמשות
