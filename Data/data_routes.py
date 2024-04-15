import numpy as np
import pandas as pd
import csv

#read the file to create the dataset
file_path = 'routes.dat'
data_list = []
with open(file_path, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        data_list.append(row)

dataset = pd.DataFrame(data_list)
column_names = ['Airline', 'Airline ID', 'Source', 'Source ID', 'Destination', 'Destination ID', 'Codeshare', 'Stops', 'Equipment']
dataset.columns = column_names

#leaving out all the non important informations
data = dataset[['Source','Destination']]

