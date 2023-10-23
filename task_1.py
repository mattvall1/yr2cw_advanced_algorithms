# Import relevant libraries
import read_data
from clrs_library.utility_functions.adjacency_matrix_graph import AdjacencyMatrixGraph


# Gather route information from the customer
starting_station = str(input('Input a starting station: '))
destination_station = str(input('Input a destination station: '))


# Get all stations required to reach destination
station_data = read_data.get_data()


# Get total duration of journey

