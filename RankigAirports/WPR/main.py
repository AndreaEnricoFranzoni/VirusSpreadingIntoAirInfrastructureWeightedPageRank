import numpy as np
import pandas as pd
import csv

#Adjacency matrix
A = pd.read_csv('A.csv', index_col = 0)

#Weights matrix
W = pd.read_csv('W.csv', index_col=0)
