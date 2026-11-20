import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
labels=['Ch. 1','Ch. 2','Ch. 3','Ch. 4','Ch. 5','Ch. 6','Ch. 7','Appendix']
a=[84,92,88,88,81,89,90,90]
b=[98,98,97,97,95,97,99,99]
fig,ax=plt.subplots(figsize=(9,4.7),layout='constrained')
x=list(range(8)); ax.bar([i-.18 for i in x],a,.36,label='First review',color='#a6aab5'); bars=ax.bar([i+.18 for i in x],b,.36,label='Final review',color='#239e85'); ax.bar_label(bars,padding=2,fontsize=9); ax.set_xticks(x,labels); ax.set_ylim(0,110); ax.set_ylabel('Reviewer score / 100'); ax.set_title('M3 — Internal agent review scores'); ax.legend(loc='lower right'); ax.spines[['top','right']].set_visible(False); fig.savefig(Path(__file__).with_name('m3_scores.png'),dpi=180)
