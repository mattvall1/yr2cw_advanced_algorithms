"""
    Author: Matthew Vallance 001225832
    Purpose: Task 1 of the coursework. This returns the time it takes to get between two user-inputted stations and the route they would need to take.
    Date: 20/10/23
"""

from clrs_library_slim.dijkstra import dijkstra
import data_processing
import utils


# Function for task_1 algorithm code
def task_1_algorithm(underground_graph, vertices, start_station, dest_station):
    # Run Dijkstra's algorithm from the clrs library to find the shortest route to all stations based on user input
    d, pi = dijkstra(underground_graph, vertices.index(start_station))
    d_dest_station = 0
    dijkstra_outputs = []
    for i in range(len(vertices)):
        # Create a sensible data structure of the output
        dijkstra_outputs.append({'dest': vertices[i], 'd': d[i], 'pi': ("None" if pi[i] is None else vertices[pi[i]])})

        # Get d for destination station
        if str(vertices[i]) == str(dest_station):
            d_dest_station = d[i]

    # Get route by looking for each predecessor in shortest path output
    route = []
    all_stations_added = False
    next_station_to_find = dest_station
    while all_stations_added is False:
        for dijkstra_output in dijkstra_outputs:
            if dijkstra_output['dest'] == str(next_station_to_find):
                # Add each station to route list to print later
                route.append(dijkstra_output['dest'])
                next_station_to_find = dijkstra_output['pi']
                # Set all_stations_added to True, this breaks the loop as we have all the details needed
                if dijkstra_output['pi'] == 'None':
                    all_stations_added = True

    return route, d_dest_station


# Get graph and vertices
underground_graph, vertices = data_processing.get_data()

# Get station inputs from the user
start_station, dest_station = utils.get_stations_from_user(vertices)

route, d_dest_station = task_1_algorithm(underground_graph, vertices, start_station, dest_station)

# TODO: Need to reverse route array at end - if needed depending on start and destination order
# Display routing
print('The shortest route for the given stations is: ' + ' -> '.join(route))

# Display time to get from start to dest
print('This will take ' + str(d_dest_station) + ' minutes.')
