"""
    Author: Matthew Vallance 001225832
    Purpose: Data visualization scripts - PAGE NOT MARKED
    Date: 25/10/23
"""
import networkx
import matplotlib as mpl
import task_1

# TODO: Use this: https://stackoverflow.com/questions/24653190/how-to-create-a-graph-using-a-csv-file-data

station_graph = networkx.from_dict_of_lists(task_1.station_data_graph)

networkx.draw_circular(station_graph, with_labels=True, node_color="magenta", edge_color="gray")

mpl.pyplot.show()