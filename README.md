# Data
Data can be found at https://openflights.org/data.php#country, in particular the dataset used is https://github.com/jpatokal/openflights/blob/master/data/routes.dat
The graph is a directed weighted graph: nodes are the ariports, edges the connections between airports, weights how many flights there are per routes.
The files `A.csv` and `W.cvs` contain respectively adjacency matrix and weight matrix.

# Goal
We want to simulate the spread of a virus all around the globe, retrieving which airports are more responsible for the spreading and eventually shut them down.
Goal of the project is to rank airport using Weighted PageRank: it will rank airports with respect their degree, strength and capability of spreading the virus (modeled through a binomial random variable, with the probability of a single success directly proportional to the number of infected people in an airport).
The highest ranked airports will contribute more to the spread: shutting them down would decrease the spread of the virus worldwide.
We want to confront this results with the spread if:
 - no airport is shut down;
 - are shut down airports ranked higher by a traditional PageRank algorithm (so, we are not taking into account anything related to the infection neither to the weights);
 - are shut down airports ranked higher by in-degree/out-degree (so, we are not taking into account anything related to the direction of the edges);
 - random airports are shut down.
The simulation of the model with airports from WPR shut down should be the best one with respect to the proportion of infected people.
We want to see the spread of three different type of virus (proportion of infection respectively: `0.1`, `0.25`, `0.5`).
Consecutively, introducing also a recovery factor in the WPR ranking.
We are taking three different initial conditions for the WPR and the simulation:
1. `2%` of people in ARL are infected. Nobody else in the world;
2. `2%` of people in FRA, CDG, AMS, IST, ATL are infected. Nobody else in the world;
3. only people in some small airports in Africa.



# AIMS
 -  Graph for the proportion of infected people worldwide vs time, for each of the virus.
 -  When airports are shut down.
 -  After having proved the goodness of WPR: graph worldwide in which we print the airports, labeled depending on their rankings.
 -  Extra: vary `gamma` and `theta` to optimize WPR.

# DONE
 - Ranking with respect to PR, yet without recovery, yet with recovey (we do not take account for infection here);
 - Ranking with respect to in-degree/out-degree, yet without recovery, yet with recovey (we do not take account for infection here);

# TODO
 - run WPR for each initial conditions, for each virus;
 - modeling of recovery factor;
 - run all the WPR inserting recovery;
 - choosing how many airports taking out from the ranking (we were doing taking the 10 highest ranked airports);
 - simulations for all WPR, with and without recovery, for all virus, for all initial conditions;
 - simulations for all PR, with and without recovery, for all virus, for all initial conditions;
 - simulations for all DC, in and out,, with and without recovery, for all virus, for all initial conditions;
 - simulations for random chosen airports, with and without recovery, for all virus, for all initial conditions;
 - saving each simulations on files in order to plot graphs of section `AIMS`.

# FILES
