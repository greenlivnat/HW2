---
name: agent-detector
description: How the reviewer-agent works in Detector mode on the compiled book: qa-super, manual page checks, layered findings, verdict.
---

# agent-detector: איתור ליקויים

המפרט המלא: `agents/reviewer_agent.md`, סעיף "מצב Detector".
1. מריצים את `qa-super`. לא מתקנים.
2. בודקים חזותית עמודים מייצגים (`pdftoppm -r 50 -f N -l N -png book.pdf out`).
3. בודקים את התוכן החדש מול המקורות ומול ה-CSV.
4. לכל ממצא: מזהה `D-...`, מיקום, קטגוריה, חומרה, שכבה ושיטתי או נקודתי.
5. השורה האחרונה בדוח: `VERDICT: PASS` או `VERDICT: REVISE`.
