import pandas as pd

A = pd.read_csv('A.csv', index_col=0)

null = ( A == 0 ).sum().sum()
sparseness= null/pow(A.shape[0],2)
print("Sparseness: ", sparseness)
s = 0