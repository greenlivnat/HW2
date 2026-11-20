import matplotlib.pyplot as plt
from pathlib import Path
p=Path(__file__).parent
fig,ax=plt.subplots(figsize=(7,3.4))
ax.barh(['Round 1: REVISE','Round 2: PASS'],[80,92], color=['#c48e38','#25967d'])
ax.invert_yaxis(); ax.set_xlim(0,100); ax.set_xlabel('Internal reviewer score / 100'); ax.set_title('Smoke test: +12 points (+15% relative)')
for i,v in enumerate([80,92]): ax.text(v-2,i,str(v),ha='right',va='center',color='white',fontweight='bold')
fig.tight_layout(); fig.savefig(p/'smoke_test_scores.png',dpi=180); plt.close(fig)
steps=['Orchestrator: launch','Research: academic source','Writer: 117 words','Reviewer: 80/100 — REVISE','API interruption and recovery','Research + Writer: correction','Reviewer: 92/100 — PASS']
fig,ax=plt.subplots(figsize=(6,8)); ax.set_xlim(0,1); ax.set_ylim(0,8); ax.axis('off')
for i,s in enumerate(steps):
 y=7.4-i*1.05; ax.text(.5,y,s,ha='center',va='center',bbox=dict(boxstyle='round,pad=.7',fc='#edf2f7',ec='#64748b'),fontsize=11)
 if i<6: ax.annotate('',xy=(.5,y-.72),xytext=(.5,y-.3),arrowprops=dict(arrowstyle='->',color='#64748b'))
fig.tight_layout(); fig.savefig(p/'smoke_test_workflow.png',dpi=180); plt.close(fig)
