"""
    Author: Matthew Vallance 001225832
    Purpose: Task 1 - Data added to graph and shortest path algorithm
    Date: 25/10/23
"""
# Import relevant libraries
import read_data
from clrs_library_slim.adjacency_list_graph import AdjacencyListGraph
from clrs_library_slim import dijkstra

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

    station_edges.append([station_id_u, station_id_v, int(connection[3])])
    # station_data_graph.insert_edge(station_id_u, station_id_v, int(connection[3]))


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


