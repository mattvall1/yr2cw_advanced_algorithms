"""
    Author: Matthew Vallance 001225832
    Purpose: Task 1 - Data added to graph and shortest path algorithm
    Date: 25/10/23
"""
import numpy as np
from testing import testing_functions

# Import relevant libraries
import read_data
from clrs_library_slim.adjacency_list_graph import AdjacencyListGraph
from clrs_library_slim import dijkstra

# Tell user the program has started
print('Preparing data...')

# Get required data
station_data, station_edges, station_list = read_data.get_data()

# Put station data into adjacency list graph - Adjust first parameter according to size of dataset
station_data_graph = AdjacencyListGraph(len(station_list), False, True)


# Add all station edges to graph
for edge in station_edges:
    station_data_graph.insert_edge(edge[0], edge[1], edge[2])


testing_functions.get_graph_csv(station_data_graph, station_list)

# Gather route information from the customer
starting_station = str(input('Input a starting station: '))
dest_station = str(input('Input a destination station: '))

# Get stations from users input
# TODO - IF TIME: Add case insensitivity here/Checks on innacurate data entry
for station in station_list:
    # Get starting station id
    if starting_station == station[1]:
        # Format: [int: id, str: station name]
        starting_station = [station[0], station[1]]
        found_match_s = True
    else:
        found_match_s = False

    # Get destination station id
    if dest_station == station[1]:
        # Format: [int: id, str: station name]
        dest_station = [station[0], station[1]]
        found_match_d = True
    else:
        found_match_d = False

# Run algorithm here to find shortest path
d, pi = dijkstra.dijkstra(station_data_graph, station[0])

print(d)
print(pi)

# Reverse d, pi
d.reverse()
pi.reverse()

# Find the indexes of both station in pi and put the smallest index first - we also want to reverse the output to display the order in which the user imputted stations
reverse_output = False
if pi.index(starting_station[0]) < pi.index(dest_station[0]):
    start_index = pi.index(starting_station[0])
    dest_index = pi.index(dest_station[0])
else:
    start_index = pi.index(dest_station[0])
    dest_index = pi.index(starting_station[0])
    reverse_output = True

# Get weight (minutes) between the stations from d - we don't want to include the station after, so index - 1 is used here
minutes_between = d[dest_index - 1]

# Get sublist of pi to find the route we're taking
stations_between = pi[start_index:dest_index + 1]

# Get all station names of sublist - this should return the routing for the users station choices
route = []
for station in stations_between:
    for station_details in station_list:
        if station_details[0] == station:
            route.append(station_details[1])

# Reverse outputs to display in the correct order
if reverse_output == True:
    route.reverse()

# Display routing
print('The shortest route for the given stations is: ' + ' -> '.join(route))

# Display time to get from start to dest
print('This will take ' + str(minutes_between) + ' minutes.')


