---
name: agent-research
description: How the research-agent finds and verifies sources for the book (pointer to the full spec).
---

# agent-research: מחקר מקורות

המפרט המלא: `agents/research_agent.md` ו-`.claude/agents/research-agent.md`.
- פלט: `docs/sources/chapter_XX.md` ואינדקס ב-`docs/SOURCES.md`.
- אסור להמציא מקורות, DOI או קישורים. כל טענה עם מיקום במקור ורמת גישה (טקסט מלא / תקציר / מטא-דאטה).
- מקבל ליקויים בקטגוריה "מקורות" מ-Detector, דרך ה-Orchestrator בלבד.
