from clrs_library_slim.adjacency_list_graph import AdjacencyListGraph
from clrs_library_slim.dijkstra import dijkstra
import read_data
import testing.testing_functions as testing_functions

station_list, station_data = read_data.get_data()


# Textbook example.
vertices = station_list
edges = station_data
# print(edges)
testing_functions.write_to_csv(edges, 'edges')
# exit()
graph1 = AdjacencyListGraph(len(vertices), False, True)

for edge in edges:
    graph1.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]), edge[2])
d, pi = dijkstra(graph1, vertices.index('Charing Cross')) # Starting station here
for i in range(len(vertices)):
    print(vertices[i] + ": d = " + str(d[i]) + ", pi = " + ("None" if pi[i] is None else vertices[pi[i]]))
