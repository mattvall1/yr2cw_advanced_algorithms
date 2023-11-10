"""
    Author: Matthew Vallance 001225832
    Purpose: Simple script to put data into a CSV for comparison externally
    Date: 20/10/23
"""

from clrs_library_slim.adjacency_list_graph import AdjacencyListGraph
from clrs_library_slim.dijkstra import dijkstra
import read_data
import testing.testing_functions as testing_functions

# Get data with appropriate variable names
vertices, edges = read_data.get_data()

# Get input from the user
# TODO: Validity check
start_station = input('Input starting station: ')
dest_station = input('Input destination station: ')

testing_functions.write_to_csv(edges, 'edges')
print_verts = []
for vetrice in vertices:
    print_verts.append([vetrice])

testing_functions.write_to_csv(print_verts, 'vertices')



# Create a graph from the clrs library for Adjacency lists
underground_graph = AdjacencyListGraph(len(vertices), False, True)

# Insert edges
for edge in edges:
    # Check if edge already exists in the graph
    existing_edges = underground_graph.get_edge_list()
    if (vertices.index(edge[0]), vertices.index(edge[1])) not in existing_edges and (vertices.index(edge[1]), vertices.index(edge[0])) not in existing_edges:
        # Insert edge into graph
        underground_graph.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]), edge[2])

testing_functions.get_graph_csv(underground_graph, vertices)
exit()
# Run Dijkstra's algorithm from the clrs library to find the shortest route to all stations based on user input
d, pi = dijkstra(underground_graph, vertices.index(start_station)) # Starting station here
for i in range(len(vertices)):
    print(vertices[i] + ": d = " + str(d[i]) + ", pi = " + ("None" if pi[i] is None else vertices[pi[i]]))
