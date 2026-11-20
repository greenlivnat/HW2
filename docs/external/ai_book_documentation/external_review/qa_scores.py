import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
labels=['Ch 1','Ch 2','Ch 3','Ch 4','Ch 5','Ch 6','Ch 7','Appendix','PDF']
before=[84,92,88,88,81,89,90,90,84]
after=[98,98,97,97,95,97,99,99,96]
x=np.arange(len(labels)); fig,ax=plt.subplots(figsize=(10,4.8))
ax.bar(x-.19,before,.38,label='First review',color='#7956D8'); ax.bar(x+.19,after,.38,label='After fixes',color='#00C9C8')
ax.set(xticks=x,xticklabels=labels,ylim=(0,105),ylabel='Internal QA score / 100',title='Review and revision across the project')
ax.legend(loc='lower right'); ax.spines[['top','right']].set_visible(False); ax.grid(axis='y',alpha=.2); ax.set_axisbelow(True)
fig.tight_layout(); fig.savefig(Path(__file__).with_name('qa_scores.png'),dpi=180); plt.close(fig)
