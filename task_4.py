"""
    Author: Matthew Vallance 001225832
    Purpose: Task 4
    Date: 14/11/23
"""
from clrs_library_slim.adjacency_list_graph import AdjacencyListGraph
from clrs_library_slim import mst
from task_1 import task_1_algorithm
import data_processing
import utils

# Get graph and vertices
underground_graph, vertices = data_processing.get_data()

# Return MST of underground_graph
underground_graph_mst = mst.kruskal(underground_graph)

# Get edge lists for both graphs - put into sets to improve time complexity O(n^2) -> O(n)
underground_graph_edges = AdjacencyListGraph.get_edge_list(underground_graph)
underground_graph_mst_edges = set(AdjacencyListGraph.get_edge_list(underground_graph_mst))

# Get removed edges
removed_edges = [x for x in underground_graph_edges if x not in underground_graph_mst_edges]

# Reassign station names to removed edges
removed_edges_names = []
for edge in removed_edges:
    removed_edges_names.append((vertices[edge[0]], vertices[edge[1]]))
    print(vertices[edge[0]] + ' -- ' + vertices[edge[1]])

# Get inputs from user
start_station, dest_station = utils.get_stations_from_user(vertices)

# Infeasibilities:
"""
 - Time: if it takes more than 100% longer to do a journey (double the time), this would be infeasible
 - No. of stations: if closing a connection means passengers would have to pass through more than 3 stations to get to thier destination (Bank -- Waterloo)
 -
"""