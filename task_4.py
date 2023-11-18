"""
    Author: Matthew Vallance 001225832
    Purpose: Task 4
    Date: 14/11/23
"""
from clrs_library_slim.adjacency_list_graph import AdjacencyListGraph
from clrs_library_slim import mst
from task_1 import task_1_algorithm
import utils


def task_4_process(graph, vertices, start, dest):
    # Return MST of underground_graph
    underground_graph_mst = mst.kruskal(graph)

    # Get edge lists for both graphs - put into sets to improve time complexity O(n^2) -> O(n)
    underground_graph_edges = AdjacencyListGraph.get_edge_list(graph)
    underground_graph_mst_edges = set(AdjacencyListGraph.get_edge_list(underground_graph_mst))

    # Get removed edges
    removed_edges = [x for x in underground_graph_edges if x not in underground_graph_mst_edges]

    # Reassign station names to removed edges
    removed_edges_names = []
    for edge in removed_edges:
        removed_edges_names.append((vertices[edge[0]], vertices[edge[1]]))
        print(vertices[edge[0]] + ' -- ' + vertices[edge[1]])

    # Get the route before and after we have run MST, so we can check feasibility of the journey
    original_route, original_time = task_1_algorithm(graph, vertices, start, dest)
    new_route, new_time = task_1_algorithm(underground_graph_mst, vertices, start, dest)

    return original_route, original_time, new_route, new_time


def run_task_4():
    # Get data
    underground_graph, underground_vertices, start_station, dest_station = utils.return_data()

    # Run the process
    original_route, original_time, new_route, new_time = task_4_process(underground_graph, underground_vertices, start_station, dest_station)
    print(original_route, new_route)

    # If the journey takes more than double the time it originally took, this is infeasible
    if (original_time * 2) < new_time:
        print('The journey between ' + start_station + ' and ' + dest_station + ' took ' + str(
            original_time) + ' minutes. It now takes ' + str(
            new_time) + ' minutes. This closure is infeasible as it takes more than double the original journey time.')

    if (len(original_route) + 3) < len(new_route):
        print('The shortest route used to be: ' + ' -> '.join(original_route) + '. It is now: ' + ' -> '.join(
            new_route) + '. This is more than 3 extra stations to complete this journey therefore its unfeasible.')

    if (original_time * 2) > new_time and (len(original_route) + 3) > len(new_route):
        print(
            'There is no notable difference in journey time or route length between ' + start_station + ' and ' + dest_station + '. This closure would be feasible.')

    # Add a newline
    print('\n')


# Only run this code if its task_4 that is run
if __name__ == "__main__":
    run_task_4()
