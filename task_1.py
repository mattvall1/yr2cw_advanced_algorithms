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


# Run Dijkstra's algorithm from the clrs library to find the shortest route to all stations based on user input
d, pi = dijkstra(underground_graph, vertices.index(start_station))
d_dest_station = 0
for i in range(len(vertices)):
    print(vertices[i] + ": d = " + str(d[i]) + ", pi = " + ("None" if pi[i] is None else vertices[pi[i]]))
    # Get d for destination station
    if str(vertices[i]) == str(dest_station):
        d_dest_station = d[i]
        # print(vertices[pi[i]])

# Change 'None' values in pi to -1 for easier coding later
pi = [-1 if x is None else x for x in pi]

# TESTING CODE
# Convert Pi into station names list:
# pi_names = []
# for x in pi:
#     if x != -1:
#         pi_names.append(vertices[x])
#     else:
#         pi_names.append('ORIGIN')
#
# d.insert(0, 'd')
# pi.insert(0, 'pi')
# pi_names.insert(0, 'PI_NAMES')
# vertices.insert(0, 'VERTS')
# testing_functions.write_to_csv([vertices, pi_names, pi, d],'dpi')

# print(pi_names)
# END TESTING CODE


# Get route - Traverse backwards?
"""
This should return as following, regardless of order the user inputs the data
    Test with Baker Street -> Edgware road. Should return: Baker Street -> Marylebone -> Edgware Road
    Test with Edgware road -> Baker Street. Should return: Edgware Road -> Marylebone -> Baker Street 
    
    Test with Edgware road -> Regents park. Should return: Edgware Road -> Marylebone -> Baker Street -> Regents park
    Test with Regents park -> Edgware road. Should return: Regents park -> Baker Street -> Marylebone -> Edgware Road
"""

"""
https://stackoverflow.com/questions/56609206/how-do-i-keep-track-of-the-shortest-paths-in-the-dijkstra-algorithm-when-using-a
You don't have to keep track of the whole path for each vertex as you've suggested. To produce the s-v paths themselves, the only thing you have to record for each vertex v is the edge that "discovered" it.

In other words, as a vertex v is being discovered by the algorithm, you record the edge (u,v) on which it achieved the value that minimized the distance from s.

Now, assuming you have the "discovering" edge for each vertex v in the graph, the path from s to v can be computed as follows: if (u,v) is the ("discovering") edge stored for v, then the shortest path from s to v is the path from s to u (which can be computed recursively), followed by the single edge (u,v).

So, to construct the shortest path from s (START) to v (DEST), you start at vertex v (DEST), then you follow the edge stored for v in the reverse direction, and continue until you reach s.
"""
route = []
all_stations_added = False
next_station_to_find = dest_station



# Display routing
print('The shortest route for the given stations is: ' + ' -> '.join(route))

# Display time to get from start to dest
print('This will take ' + str(d_dest_station) + ' minutes.')
