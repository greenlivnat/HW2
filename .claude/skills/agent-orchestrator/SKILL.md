---
name: agent-orchestrator
description: Procedure for the main Claude Code session acting as Orchestrator of the book: plan, invoke one sub-agent at a time, gate, document, keep the STATUS recovery point.
---

# agent-orchestrator: נוהל סוכן-העל

מקור האמת: `CLAUDE.md` ו-`agents/orchestrator_agent.md`. כאן רק סדר הפעולות.

1. קוראים את `docs/STATUS.md`, ומתחילים מהחבילה הראשונה שלא סומנה ✅ בטבלת נקודת ההתאוששות.
2. **סוכן אחד בכל רגע.** כתיבה: writer-agent. איתור: reviewer-agent במצב Detector. תיקון: fixer-agent. מקורות: research-agent.
3. אחרי כל הפעלה: שער (`git status`, הקבצים הצפויים, `python scripts/qa.py <skill>` הרלוונטי), תיעוד ב-`agents/runs/<agent>_<unit>_r<N>.md`, ורשומה ב-`docs/PROMPT_HISTORY.md`.
4. ליקוי שיטתי מתקנים בכלי (CLS, ממיר או Skill) ומתעדים ב-`docs/INCIDENTS.md`.
5. בסוף כל חבילה מעדכנים את STATUS §0. במגבלת שימוש או בכשל חוזר: שומרים ועוצרים.
6. Commit רק לפי בקשה. אין push לפני M7.
