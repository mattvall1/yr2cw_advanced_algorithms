"""
    Author: Matthew Vallance 001225832, Deanna White 001208356, Varnika Mogali 001279858, Kayleigh Harmsworth 001218868, Deeya Patel 001230057
    Purpose: Data imports from London Underground CSV
    Date: 16/10/23
"""
import csv
from clrs_library_slim.adjacency_list_graph import AdjacencyListGraph


# Return an array of the nodes in the graph
def remove_duplicate_stations(station_list) -> list:
    return list(set(station_list))


def create_underground_graph(vertices, edges):
    # Create a graph from the clrs library for Adjacency lists
    underground_graph = AdjacencyListGraph(len(vertices), False, True)

    # Insert edges
    for edge in edges:
        # Check if edge already exists in the graph
        existing_edges = underground_graph.get_edge_list()
        if (vertices.index(edge[0]), vertices.index(edge[1])) not in existing_edges and (
                vertices.index(edge[1]), vertices.index(edge[0])) not in existing_edges:
            # Insert edge into graph
            underground_graph.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]), edge[2])

    return underground_graph


# Get data from CSV and format into appropriate data structure - using above functions
def get_data():
    # Open and read CSV file
    # with open('data/random_data.csv', 'r') as file: # Random data consisting of edges made of the alphabet
    # with open('data/small_data.csv', 'r') as file: # Uncomment for testing on one line - Bakerloo
    # with open('data/medium_data.csv', 'r') as file: # Uncomment for testing on two lines - Bakerloo + Central
    # with open('data/large_data.csv', 'r') as file: # Uncomment for testing on three lines - Bakerloo + Central + Circle
    with open('data/london_underground_data.csv', 'r') as file:
        # Read CSV file
        data = csv.reader(file)

        # Put data into an appropriate data structure
        station_data = []  # edges
        station_list = []  # nodes in the graph
        for line in data:
            # Add connections with times to an array
            if line[2] != '':
                # Format: [str: start station, str: dest. station, int: time between stations]
                station_data.append(
                    [line[1].rstrip().replace('\'', ''), line[2].rstrip().replace('\'', ''), int(line[3])])

            # Create a list of stations
            if line[2] == '':
                station_list.append(line[1].rstrip().replace('\'', ''))

    # Remove duplicate stations
    station_list_no_duplicates = remove_duplicate_stations(station_list)

    # Create the graph
    underground_graph = create_underground_graph(station_list_no_duplicates, station_data)

    return [underground_graph, station_list_no_duplicates]
