"""
    Author: Matthew Vallance 001225832
    Purpose: Task 1 of the coursework. This returns the time it takes to get between two user-inputted stations and the route they would need to take.
    Date: 20/10/23
"""
import time

from clrs_library_slim.dijkstra import dijkstra
import utils


# Function for task_1 algorithm code
def task_1_algorithm(graph, vertices, start, dest):
    # Run Dijkstra's algorithm from the clrs library to find the shortest route to all stations based on user input
    d, pi = dijkstra(graph, vertices.index(start))
    d_dest_station = 0
    dijkstra_outputs = []
    for i in range(len(vertices)):
        # Create a sensible data structure of the output
        dijkstra_outputs.append({'dest': vertices[i], 'd': d[i], 'pi': ("None" if pi[i] is None else vertices[pi[i]])})

        # Get d for destination station
        if str(vertices[i]) == str(dest):
            d_dest_station = d[i]

    # Get route by looking for each predecessor in shortest path output
    route = []
    all_stations_added = False
    next_station_to_find = dest
    while all_stations_added is False:
        for dijkstra_output in dijkstra_outputs:
            if dijkstra_output['dest'] == str(next_station_to_find):
                # Add each station to route list to print later
                route.append(dijkstra_output['dest'])
                next_station_to_find = dijkstra_output['pi']
                # Set all_stations_added to True, this breaks the loop as we have all the details needed
                if dijkstra_output['pi'] == 'None':
                    all_stations_added = True

    # Reverse the route to display correctly
    route.reverse()

    return route, d_dest_station


def run_task_1(get_timings = False):
    # Get data
    underground_graph, underground_vertices, start_station, dest_station = utils.return_data()

    # If we want the efficiency, we time the algorithm
    if get_timings:
        start_time = time.time()

    # Run the algorithm
    route, dest_time = task_1_algorithm(underground_graph, underground_vertices, start_station, dest_station)

    if get_timings:
        end_time = time.time()
        print('Timing: ' + str(round((end_time - start_time), 3)) + 's')

    # Display routing
    print('The shortest route for the given stations is: ' + ' -> '.join(route))

    # Display time to get from start to dest
    print('This will take ' + str(dest_time) + ' minutes.\n')


# Only run this code if its task_1 that is run
if __name__ == "__main__":
    run_task_1()
