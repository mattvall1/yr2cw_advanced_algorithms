"""
    Author: Matthew Vallance 001225832
    Purpose: Task 3 - Revised task_2 but with the Bellman Ford Algorithm
    Date: 23/10/23
"""

from clrs_library_slim.bellman_ford import bellman_ford
import data_processing
import utils

# Get graph and vertices
underground_graph, vertices = data_processing.get_data()

# Get station inputs from the user
start_station, dest_station = utils.get_stations_from_user(vertices)

# Run Bellman Ford algorithm from the clrs library to find the shortest route to all stations based on user input
d, pi, negative_weight_cycle = bellman_ford(underground_graph, vertices.index(start_station))
bellman_outputs = []
for i in range(len(vertices)):
    # Create a sensible data structure of the output
    bellman_outputs.append({'dest': vertices[i], 'd': d[i], 'pi': ("None" if pi[i] is None else vertices[pi[i]])})


# Get route by looking for each predecessor in shortest path output
route = []
all_stations_added = False
next_station_to_find = dest_station
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
route.reverse()

# Display routing
print('The shortest route for the given stations is: ' + ' -> '.join(route))

# Display count of stations to get to the destination minus 2 - we only want the count of stations in between
print('You will pass through ' + str(station_count - 2) + ' stations on your journey.')

# ? missing 3b
# Your team must also produce a histogram of the journey times (in the count of stations or
# stops) between every station pair, utilising the calculations from the previous subtask (3a).