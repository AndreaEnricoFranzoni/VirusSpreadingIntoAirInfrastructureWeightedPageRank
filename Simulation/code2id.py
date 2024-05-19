import csv

import pandas as pd

airports_file_path = '../Data/airports.dat'

data_list = []
with open(airports_file_path, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        data_list.append(row)

dataset_airport = pd.DataFrame(data_list)
dataset_airport.columns = ['Airport ID', 'Name', 'City', 'Country', 'IATA', 'ICAO', 'Latitude', 'Longitude', 'Altitude',
                           'Timezone', 'DST',
                           'Tz database timezone', 'Type', 'Source']

ranking_file_path = '../RankingResults/WPR/without_recovery/Arlanda/results_WPR_nr_ARN_alpha1.csv'

data_list = []
with open(ranking_file_path, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        data_list.append(row)

dataset_ranking = pd.DataFrame(data_list)
dataset_ranking.columns = ['ID', 'Code', 'Value']

result = []
counter = 0
for _, item in dataset_ranking.iterrows():
    if counter == 101:
        break
    counter += 1
    for _, airport in dataset_airport.iterrows():
        if airport['IATA'] == item['Code']:
            result.append(int(airport['Airport ID']))
            break
print(result)
