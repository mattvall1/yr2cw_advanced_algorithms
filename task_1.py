"""
    Author: Matthew Vallance 001225832
    Purpose: Task 1 - Data added to graph and shortest path algorithm
    Date: 25/10/23
"""
import numpy as np

# Import relevant libraries
import read_data
from clrs_library_slim.adjacency_list_graph import AdjacencyListGraph
from clrs_library_slim import dijkstra
from testing import data_to_csv

# Tell user the program has started
print('Preparing data...')

# Get required data
station_data, station_list = read_data.get_data()

# Put station data into adjacency list graph - Adjust first parameter according to size of dataset
station_data_graph = AdjacencyListGraph(len(station_list), False, True)

# Create list of edges to insert also create a set to store sorted tuples - for checking duplicates
station_edges = []
edge_set = set()
for connection in station_data:
    # Get station edges to insert into array
    station_id_u = 0
    station_id_v = 0
    for station in station_list:
        # Start
        if connection[1] == station[1]:
            station_id_u = station[0]
        # Destination
        if connection[2] == station[1]:
            station_id_v = station[0]

    # Check edge against all previous results and add to station_edges if no duplicates are found
    station_edges.append([sorted([station_id_u, station_id_v]), int(connection[3])])

# Sort all edges so we can remove duplicates and find the shortest time between the duplicates
station_edges = sorted(station_edges)
station_edges_cleaned = []
for i in range(1, len(station_edges)):
    # Get the shortest routes between each station (regardless of line)
    if station_edges[i][0] != station_edges[i - 1][0]:
        station_edges_cleaned.append([[station_edges[i][0][0], station_edges[i][0][1]], station_edges[i][1]])
    else:
        # Keep edges which have a smaller weight than the last item, or if they are equal (we remove these later)
        if station_edges[i][1] < station_edges[i - 1][1] or station_edges[i][1] == station_edges[i - 1][1]:
            station_edges_cleaned.append([[station_edges[i][0][0], station_edges[i][0][1]], station_edges[i][1]])

# Run sorting algorithm twice to make sure we catch everything
# TODO: Make this less crap
station_edges_cleaned_2 = []
for i in range(1, len(station_edges_cleaned)):
    # Get the shortest routes between each station (regardless of line)
    if station_edges_cleaned[i][0] != station_edges_cleaned[i - 1][0]:
        station_edges_cleaned_2.append([station_edges_cleaned[i][0][0], station_edges_cleaned[i][0][1], station_edges_cleaned[i][1]])
    else:
        # Keep edges which have a smaller weight than the last item, or if they are equal (we remove these later)
        if station_edges_cleaned[i][1] < station_edges_cleaned[i - 1][1] or station_edges_cleaned[i][1] == station_edges_cleaned[i - 1][1]:
            station_edges_cleaned_2.append([station_edges_cleaned[i][0][0], station_edges_cleaned[i][0][1], station_edges_cleaned[i][1]])

# Convert list of edges to tuples to remove duplicates, then convert back to list of lists
station_edges_set = set(tuple(x) for x in station_edges_cleaned_2)
station_edges_cleaned_2 = [list(x) for x in station_edges_set]

data_to_csv.write_to_csv(sorted(station_edges_cleaned_2), 'edges')
# exit()

# Add all station edges to graph
for edge in station_edges_cleaned_2:
    # Remove self loops before inserting edge
    if edge[0] != edge[1]:
        station_data_graph.insert_edge(edge[0], edge[1], edge[2])


# Gather route information from the customer
starting_station = str(input('Input a starting station: '))
dest_station = str(input('Input a destination station: '))

# Get stations from users input
# TODO - IF TIME: Add case insensitivity here
for station in station_list:
    # Get starting station id
    if starting_station == station[2]:
        # Format: [int: id, str: station name]
        starting_station = [station[0], station[2]]
        found_match_s = True
    else:
        found_match_s = False

    # Get destination station id
    if dest_station == station[2]:
        # Format: [int: id, str: station name]
        dest_station = [station[0], station[2]]
        found_match_d = True
    else:
        found_match_d = False

# TODO: Run algorithm here to find shortest path


# TODO: Display routing here

# TODO: Display time to get from start to dest here


