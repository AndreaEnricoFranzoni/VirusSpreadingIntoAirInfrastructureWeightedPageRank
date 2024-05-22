import numpy as np
import pandas as pd
from BFS import BFS


'''
To calculate it:

A = pd.read_csv('A.csv', index_col=0).to_numpy()

n = A.shape[0]
GiantComponent = np.zeros(n,dtype=int)

label_GC = 1
for i in range(n):

    if(GiantComponent[i]==0):
        GiantComponent[i] = label_GC

    temp = BFS(A,i)

    for j in range(n):
        if temp[j]!=0 and GiantComponent[j]==0:
            GiantComponent[j] = label_GC

    label_GC += 1
'''



GC = pd.read_csv('GC.csv', index_col=0)
n = GC.shape[0]

elemets_per_GC = np.zeros(n,dtype=int)

for i in range(n):
    elemets_per_GC[i] = (GC == i+1).sum().sum()

label_GC = range(n) + np.ones(n,dtype=int)
GC_quantities = pd.DataFrame(data=elemets_per_GC,index=label_GC)
s = 0






