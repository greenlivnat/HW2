# PLAN: תוכנית העבודה

> **עודכן:** 2026-11-18 (PRD 1.5). המצב השוטף ונקודת ההתאוששות נמצאים ב-`docs/STATUS.md`. המשימות הפתוחות ב-`docs/TODO.md`.

## אבני דרך
| אבן דרך | תוכן | מצב |
|---|---|---|
| M1 | PRD, מבנה, ארכיטקטורת סוכנים, Smoke Test | ✅ |
| M2 | מחקר מקורות (research-agent) | ✅ |
| M3 | 7 פרקים ונספח (writer ← reviewer, עד 3 סבבים) | ✅ |
| **M4** | ניסוי UCI Digits, ‏11 המחשות (VISUALS.md) ועוד איור הנספח, טבלאות | ✅ (ממתין לאישור) |
| **M5A** | ‏CLS, ממיר TXT←TeX, ‏LuaLaTeX ו-biber, ‏IEEE, ‏Detector ← Fixer, ‏PDF ראשוני מלא, סקריפט בנייה | ✅ (ממתין לאישור) |
| M5B | ליטוש לפי משוב המשתמשת על ה-PDF הראשוני | ⏳ |
| M6 | ביקורת סופית (Detector), ‏README עם צילומי מסך, עדכון אחרון לנספח | ⏳ |
| M7 | ‏push ל-`https://github.com/greenlivnat/HW2` והגשה | ⏳ רק אחרי אישור |

## צינור ההפקה (בר-שחזור)
```
chapters/*.txt ──scripts/txt2tex.py──► latex/chapters/*.tex ─┐
chapters/*.txt ──scripts/make_bib.py─► references.bib ───────┤
python/experiment_config.json ─► python/generate_chart.py ─► python/data/*.csv ─► python/make_figures.py ─► assets/charts/*.pdf ─┤
latex/figures/*.tex (TikZ) ──────────────────────────────────┤
latex/aibook.cls + main.tex ──latexmk (LuaLaTeX + biber)─────┴► main.pdf ─► book.pdf ─► scripts/qa.py super
```
פקודה אחת: `python scripts/build.py` (ועם `--experiment` גם הניסוי).

## חלוקת אחריות בין הסוכנים (M4/M5A)
| עבודה | מבצע |
|---|---|
| ניסוי, איורים, CLS, ממיר, בנייה ו-QA (כלים דטרמיניסטיים) | Orchestrator |
| השלמת 4 המקומות בפרק 5, תקציר ומילות מפתח, עדכון הנספח | writer-agent |
| בדיקת הספר המהודר (qa-super ובדיקה ידנית) | reviewer-agent במצב Detector |
| 19 הליקויים הקלים מ-M3, וממצאי Detector בשכבת ה-TXT | fixer-agent |
| ליקויים שיטתיים (CLS, ממיר, Skills) | Orchestrator, עם רשומה ב-`docs/INCIDENTS.md` |

## כללי עבודה
סוכן אחד בכל רגע; מודל חסכוני (sonnet) לכתיבה, איתור ותיקון; נקודת התאוששות ב-STATUS אחרי כל חבילה; commit מקומי בלבד.
