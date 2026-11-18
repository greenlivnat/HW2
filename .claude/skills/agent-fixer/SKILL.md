---
name: agent-fixer
description: How the fixer-agent applies minimal fixes from a Detector report and escalates systematic defects.
---

# agent-fixer: תיקון

המפרט המלא: `agents/fixer_agent.md`.
1. מקבלים רשימת מזהים ודוח. מתקנים רק בקבצים שהוקצו, במינימום שינוי.
2. ליקוי שיטתי עובר ל-Orchestrator, לתיקון בכלי. ליקוי שדורש מקור עובר ל-Research.
3. מחזירים טבלה: מזהה, מיקום, לפני ואחרי, סטטוס. בלי ציון ובלי VERDICT.
