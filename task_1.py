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
station_data = read_data.get_data()[0]
station_list = read_data.get_data()[1]

print(station_list)
print(station_data)

# Put station data into adjacency matrix - Adjust first parameter according to size of dataset - WE CAN DO THIS AUTOMATICALLY LATER
# TODO: Use len(station_list) here, after testing
station_data_graph = AdjacencyListGraph(5, False, True)

for station_details in station_data:
    # Get station keys to insert into matrix
    for station in station_list:
        if station_details[0] == station[2]:
            station_id_u = station[0]
        elif station_details[1] == station[2]:
            station_id_v = station[0]

    # print(station_id_u)
    # print(station_id_v)
    # print(station_details)

    station_data_graph.insert_edge(station_id_u, station_id_v, int(station_details[2]))

print(station_data_graph.get_edge_list())

# Gather route information from the customer
starting_station = str(input('Input a starting station: '))
dest_station = str(input('Input a destination station: '))

# Get stations from users input -
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
d, pi = dijkstra(station_data_graph, )


print(dijkstra.dijkstra(station_data_graph, 1))

# TODO: Display routing here

# TODO: Display time to get from start to dest here


