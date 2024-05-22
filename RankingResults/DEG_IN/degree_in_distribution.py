import pandas as pd
import matplotlib.pyplot as plt



deg = pd.read_csv('results_deg_in.csv', index_col=0)



figure, graph = plt.subplots()
graph.hist(x = deg["Ranking"],
             bins = 13,
             ec = "grey",
             fc = "blue" )

graph.set_xlabel("In-degree")
graph.set_ylabel("Frequency")
graph.set_title("In-degree distribution")

plt.show()


