"""
    Author: Matthew Vallance 001225832
    Purpose: Task 4
    Date: 14/11/23
"""
from clrs_library_slim import mst
import read_data

# Get graph and vertices
underground_graph, vertices = read_data.get_data()

# Return MST of underground_graph
underground_graph_mst = mst.kruskal(underground_graph)

# Get edge lists for both graphs
underground_graph_edges = AdjacencyListGraph.get_edge_list(underground_graph)
underground_graph_mst_edges = AdjacencyListGraph.get_edge_list(underground_graph_mst)

# Get removed edges
removed_edges = [x for x in underground_graph_edges if x not in underground_graph_mst_edges]

# Reassign station names to removed edges
removed_edges_names = []
for edge in removed_edges:
    removed_edges_names.append((vertices[edge[0]], vertices[edge[1]]))
    print(vertices[edge[0]] + ' -- ' + vertices[edge[1]])

# TODO: Ask user to input two stations, so we can check feasibility of removing the link between them


