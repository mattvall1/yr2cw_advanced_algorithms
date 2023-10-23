# Import relevant libraries
import read_data
from clrs_library.utility_functions.adjacency_matrix_graph import AdjacencyMatrixGraph


# Gather route information from the customer
starting_station = str(input('Input a starting station: '))
destination_station = str(input('Input a destination station: '))


# Get required data
station_data = read_data.get_data()[0]
station_list = read_data.get_data()[1]

# print(station_list)
# print(station_data)

exit()

# Put station data into adjacency matrix
station_data_graph = AdjacencyMatrixGraph(5, True, True)

for station in station_data:
    print(station)
    station_data_graph.insert_edge(station[1], station[2], int(station[3]))


# Get total duration of journey





