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
station_data, station_edges, station_list = read_data.get_data()

data_to_csv.write_to_csv(station_data, 'station_data')
data_to_csv.write_to_csv(station_edges, 'station_edges')
data_to_csv.write_to_csv(sorted(station_list), 'station_list')

# Put station data into adjacency list graph - Adjust first parameter according to size of dataset
station_data_graph = AdjacencyListGraph(len(station_list), False, True)


# Add all station edges to graph
for edge in station_edges:
    station_data_graph.insert_edge(edge[0], edge[1], edge[2])

print(station_data_graph)

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


