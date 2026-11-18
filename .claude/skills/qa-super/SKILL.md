---
name: qa-super
description: Run every deterministic quality check of the Hebrew AI book and write one report. Use after each build, before a Detector review, and before any commit of the PDF.
---

# qa-super: כל בדיקות האיכות בהרצה אחת

**מי מפעיל:** Detector (reviewer-agent במצב Detector) או ה-Orchestrator אחרי בנייה.
**פקודה:** `python -X utf8 scripts/qa.py super` (קריאה בלבד, חוץ מכתיבת הדוח).
**פלט:** `agents/runs/qa/qa_report.md` ו-`qa_report.json`. קוד יציאה 1 אם יש FAIL.

## מה רץ
qa-BiDi, ‏qa-table, ‏qa-code, ‏qa-img, ‏qa-typeset, ‏qa-infra, ‏qa-cls-version. פירוט כל אחד ב-SKILL.md שלו.

## איך מפרשים
- **FAIL** חוסם מעבר לשלב הבא. WARN נבדק ידנית ומתועד.
- לכל FAIL קובעים **שכבה** (TXT / ממיר / CLS / איור / סקריפט) ו**שיטתי או נקודתי**. ליקוי שיטתי מתוקן בכלי שמייצר אותו (Skill, ‏CLS או ממיר), ולא בקובץ הפלט.
- הבדיקות האוטומטיות אינן מחליפות מבט בעמודים: אחרי qa-super בודקים חזותית לפחות שער, פתיחת פרק, איור, טבלה, נוסחה ותרשים (PRD §11).
