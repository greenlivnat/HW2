import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
p=Path(__file__).resolve().parent
usable=np.array([8,12,3,8,10,10,10]); total=np.array([10,14,4,8,11,13,13])
fig,ax=plt.subplots(figsize=(9,5)); x=np.arange(1,8)
ax.bar(x,usable,label='Usable records'); ax.bar(x,total-usable,bottom=usable,label='Other records'); ax.set(xlabel='Chapter',ylabel='Source records',title='M2 research coverage — 61 of 73 records usable',xticks=x); ax.legend(); fig.tight_layout(); fig.savefig(p/'m2_sources.png',dpi=180); plt.close(fig)
fig,ax=plt.subplots(figsize=(5,5)); ax.pie([61,12],labels=['Usable','Other'],autopct='%1.1f%%',wedgeprops={'width':.35}); ax.set_title('M2 source eligibility (reported)'); fig.tight_layout(); fig.savefig(p/'m2_eligibility.png',dpi=180)
