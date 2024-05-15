import csv

import pandas as pd


def get_all_degrees():
    airports_dat = '../Data/routes.dat'
    degree_sum = {}

    data_list = []
    with open(airports_dat, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            data_list.append(row)

    dataset = pd.DataFrame(data_list)
    dataset.columns = ['Airline', 'Airline ID', 'Source airport', 'Source airport ID', 'Destination airport',
                       'Destination airport ID', 'Codeshare', 'Stops', 'Equipment']

    for _, route in dataset.iterrows():
        if not route['Source airport ID'] == '\\N':
            if int(route['Source airport ID']) not in degree_sum:
                degree_sum[int(route['Source airport ID'])] = 1
            else:
                degree_sum[int(route['Source airport ID'])] += 1
        if not route['Destination airport ID'] == '\\N':
            if int(route['Destination airport ID']) not in degree_sum:
                degree_sum[int(route['Destination airport ID'])] = 1
            else:
                degree_sum[int(route['Destination airport ID'])] += 1

    return degree_sum
