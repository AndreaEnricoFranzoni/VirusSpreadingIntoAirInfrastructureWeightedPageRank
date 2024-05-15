import pandas as pd
import plotly.express as px


airports_data = pd.read_csv('airports.csv')
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