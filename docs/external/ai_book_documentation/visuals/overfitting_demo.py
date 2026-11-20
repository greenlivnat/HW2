import matplotlib.pyplot as plt
from pathlib import Path
out=Path(__file__).resolve().parent
x=[1,2,3,4,5]; train=[62,74,82,89,95]; test=[59,69,75,76,72]
plt.figure(figsize=(8,4.5)); plt.plot(x,train,marker='o',label='Training'); plt.plot(x,test,marker='o',label='Test'); plt.xlabel('Epoch'); plt.ylabel('Illustrative accuracy (%)'); plt.title('Overfitting illustration — synthetic data'); plt.xticks(x); plt.legend(); plt.tight_layout(); plt.savefig(out/'overfitting_demo.png',dpi=180); plt.close()
