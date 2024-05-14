import numpy as np
import pandas as pd
import plotly.express as px

from DEG import DEG
from WPR import WPR

airports_data = pd.read_csv('airports.csv')

A = pd.read_csv('A.csv', index_col=0)  # Adjacency matrix
W = pd.read_csv('W.csv', index_col=0)  # Weights matrix


<<<<<<< HEAD
=======

# At every airport there is one infected person.
# Since there is no recovery atm, everybody will be infected after just a few time steps.
initially_infected_at_airports = np.ones(A.shape[0], dtype=float)
# initially_infected_at_airports[A.keys().tolist().index("ARN")] = 1

wpr = WPR(A.to_numpy(), W.to_numpy(), 0.95, 0.9, 0.45, initially_infected_at_airports)

# Rank airports.
# WPR
# wpr.converge(1, 25)
# PR


# ranks_wpr = wpr.ranks

airports = A.keys().tolist()

# pr = PR(A.to_numpy(), 0.95)
# pr.converge(1, 2)
# ranks_pr = pr.ranks
# idx_sort_pr = ranks_pr.argsort()

deg = DEG(A.to_numpy())
ranks_deg = np.array(deg.degree_in)
idx_sort_deg = ranks_deg.argsort()


# idx_sort = range(len(ranks)) # Sorts alphabetically.

for airport_idx in idx_sort_deg:
    print("{airport}: {value}".format(airport=airports[airport_idx], value=ranks_deg[airport_idx]))

def draw_map():
    color_scale = [(0, 'orange'), (1, 'red')]
    fig = px.scatter_mapbox(
        airports_data,
        lat="Latitude",
        lon="Longitude",
        hover_name="Name",
        hover_data=["IATA", "ICAO"],
        # color="Listed",
        # color_continuous_scale=color_scale,
        # size="Listed",
        zoom=8,
        height=800,
        width=1600
    )
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

# draw_map()
>>>>>>> 49dc6c9e5cbc8d13dd23c57b800298803206060d
