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

    # Get the route before and after we have run MST, so we can check feasibility of the journey
    original_route, original_time = task_1_algorithm(graph, vertices, start, dest)
    new_route, new_time = task_1_algorithm(underground_graph_mst, vertices, start, dest)

    # Reverse the routes to display correctly
    original_route.reverse()
    new_route.reverse()

    return original_route, original_time, new_route, new_time, removed_edges_names


def run_task_4():
    # While loop to make sure user inputs valid stations
    stations_together = False
    while not stations_together:
        # Get data
        underground_graph, underground_vertices, start_station, dest_station = utils.return_data()

        # Run the process
        original_route, original_time, new_route, new_time, removed_edges_names = task_4_process(underground_graph, underground_vertices, start_station, dest_station)

        # Check the stations are together - if not, we ask the user to re-enter inputs
        if len(original_route) > 2:
            print('The stations you entered are not adjacent. Try again.')
            stations_together = False
        else:
            stations_together = True

    # If the journey takes more than triple the time it originally took, this is infeasible
    if (original_time * 3) < new_time:
        print('The journey between ' + start_station + ' and ' + dest_station + ' took ' + str(
            original_time) + ' minutes. It now takes ' + str(
            new_time) + ' minutes. This closure is infeasible as it takes more than double the original journey time.')

    # If the new route has more than 3 extra stops, this is infeasible
    if (len(original_route) + 3) < len(new_route):
        print('The shortest route used to be: ' + ' -> '.join(original_route) + '. It is now: ' + ' -> '.join(
            new_route) + '. This is more than 3 extra stations to complete this journey therefore its unfeasible.')

    # If neither of these apply, it is feasible
    if (original_time * 2) > new_time and (len(original_route) + 3) > len(new_route):
        print('There is no notable difference in journey time or route length between ' + start_station + ' and ' + dest_station + '. This closure would be feasible.')
        print(start_station + ' -- ' + dest_station)

    # Ask the user if they want to view all closures
    view_closures = ''
    while view_closures != 'Y':
        view_closures = input('View all possible closures - regardless of feasibility? (Y/N): ')
        if view_closures == 'Y':
            for edge in removed_edges_names:
                print(edge[0] + ' -- ' + edge[1])
        elif view_closures == 'N':
            print('Not a valid option.')
        else:
            break

    # Add a newline
    print('\n')


# Only run this code if its task_4 that is run
if __name__ == "__main__":
    run_task_4()
