"""
    Author: Matthew Vallance 001225832
    Purpose: Task 3 - Revised task_2 but with the Bellman Ford Algorithm
    Date: 23/10/23
"""
import time

from clrs_library_slim.bellman_ford import bellman_ford
import utils


def task_3_algorithm(graph, vertices, start, dest):
    # Run Bellman Ford algorithm from the clrs library to find the shortest route to all stations based on user input
    d, pi, negative_weight_cycle = bellman_ford(graph, vertices.index(start))
    bellman_outputs = []
    for i in range(len(vertices)):
        # Create a sensible data structure of the output
        bellman_outputs.append({'dest': vertices[i], 'd': d[i], 'pi': ("None" if pi[i] is None else vertices[pi[i]])})

    # Get route by looking for each predecessor in shortest path output
    route = []
    all_stations_added = False
    next_station_to_find = dest
    station_count = 0
    while all_stations_added is False:
        for bellman_output in bellman_outputs:
            if bellman_output['dest'] == str(next_station_to_find):
                # Add each station to route list to print later
                route.append(bellman_output['dest'])
                next_station_to_find = bellman_output['pi']
                station_count += 1
                # Set all_stations_added to True, this breaks the loop as we have all the details needed
                if bellman_output['pi'] == 'None':
                    all_stations_added = True

    # Reverse the route to display correctly
    route.reverse()

    return route, station_count


def run_task_3(get_timings = False):
    # Get data
    underground_graph, underground_vertices, start_station, dest_station = utils.return_data()

    # If we want the efficiency, we time the algorithm
    if get_timings:
        start_time = time.time()

    # Run the algorithm
    route, station_count = task_3_algorithm(underground_graph, underground_vertices, start_station, dest_station)

    if get_timings:
        end_time = time.time()
        print('Timing: ' + str(round((end_time - start_time), 3)) + 's')

    # Display routing
    print('The shortest route for the given stations is: ' + ' -> '.join(route))

    # Display count of stations to get to the destination minus 2 - we only want the count of stations in between
    print('You will pass through ' + str(station_count - 2) + ' stations on your journey.\n')


# Only run this code if its task_3 that is run
if __name__ == "__main__":
    run_task_3()
