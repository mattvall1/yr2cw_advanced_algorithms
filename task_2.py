"""
    Author: Matthew Vallance 001225832
    Purpose: Task 2 of the coursework. This returns the number of stops between two user-inputted stations and the route they would need to take.
    Date: 5/11/23
"""

from clrs_library_slim.dijkstra import dijkstra
from testing import testing_functions
import data_processing
import utils

# Get graph and vertices
underground_graph, vertices = data_processing.get_data()

# FOR HISTOGRAM CREATION:
# testing_functions.get_graph_csv_task_2(underground_graph, vertices)
# exit()

# Get station inputs from the user
start_station, dest_station = utils.get_stations_from_user(vertices)

# Run Dijkstra's algorithm from the clrs library to find the shortest route to all stations based on user input
d, pi = dijkstra(underground_graph, vertices.index(start_station))
dijkstra_outputs = []
for i in range(len(vertices)):
    # Create a sensible data structure of the output
    dijkstra_outputs.append({'dest': vertices[i], 'd': d[i], 'pi': ("None" if pi[i] is None else vertices[pi[i]])})


# Get route by looking for each predecessor in shortest path output
route = []
all_stations_added = False
next_station_to_find = dest_station
station_count = 0
while all_stations_added is False:
    for dijkstra_output in dijkstra_outputs:
        if dijkstra_output['dest'] == str(next_station_to_find):
            # Add each station to route list to print later
            route.append(dijkstra_output['dest'])
            next_station_to_find = dijkstra_output['pi']
            station_count += 1
            # Set all_stations_added to True, this breaks the loop as we have all the details needed
            if dijkstra_output['pi'] == 'None':
                all_stations_added = True
route.reverse()

# Display routing
print('The shortest route for the given stations is: ' + ' -> '.join(route))

# Display count of stations to get to the destination minus 2 - we only want the count of stations in between
print('You will pass through ' + str(station_count - 2) + ' stations on your journey.')


# ? where is the histogram of the journey times
# Your team must also produce a histogram of the journey times (in the count of stations or
# stops) between every station pair, utilizing the calculations from the previous subtask (2a).