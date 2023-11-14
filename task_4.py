"""
    Author: Matthew Vallance 001225832
    Purpose: Task 4
    Date: 14/11/23
"""
from clrs_library_slim import mst
from clrs_library_slim.adjacency_list_graph import AdjacencyListGraph
import read_data

# Get data with appropriate variable names
vertices, edges = read_data.get_data()

# Create a graph from the clrs library for Adjacency lists
underground_graph = AdjacencyListGraph(len(vertices), False, True)

# Insert edges
for edge in edges:
    # Check if edge already exists in the graph
    existing_edges = underground_graph.get_edge_list()
    if (vertices.index(edge[0]), vertices.index(edge[1])) not in existing_edges and (vertices.index(edge[1]), vertices.index(edge[0])) not in existing_edges:
        # Insert edge into graph
        underground_graph.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]), edge[2])

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

