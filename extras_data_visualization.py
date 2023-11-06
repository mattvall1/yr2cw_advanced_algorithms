"""
    Author: Matthew Vallance 001225832
    Purpose: Data visualization scripts - PAGE NOT MARKED
    Date: 25/10/23
"""
import networkx as nx
import matplotlib.pyplot as plt
import read_data

# TODO: Use this: https://stackoverflow.com/questions/24653190/how-to-create-a-graph-using-a-csv-file-data

edges = read_data.get_data()[1]

G = nx.Graph()
for edge in edges:
    print(edge)
    G.add_edge(edge[0], edge[1], weight=edge[2])  # specify edge data

pos = nx.random_layout(G)
plt.figure(figsize=(10, 10), dpi=1000)
nx.draw(G, pos)
nx.draw_networkx_edge_labels(G, pos)
plt.show()