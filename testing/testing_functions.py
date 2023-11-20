"""
    Author: Matthew Vallance 001225832
    Purpose: Simple script to put data into a CSV for comparison externally
    Date: 26/10/23
"""
import csv
import random
import time
from clrs_library_slim import dijkstra
import task_3


def write_to_csv(data, filename='testing_data'):
    # Routine to output any data into CSVs
    with open("testing/csv_output/"+filename+".csv", "w") as file_to_write:
        # Create writer to write row
        writer = csv.writer(file_to_write)
        # Write each row of data to the CSV file
        for row in data:
            writer.writerow(row)
        print('Generated ' + filename + '.csv')


def get_graph_csv(station_data_graph, vertices):
    # Routine to output all stations to all stations upon completion of Dijkstra's algorithm
    output = []
    top_column = ['']
    # Build a CSV
    for i in vertices:
        d, pi = dijkstra.dijkstra(station_data_graph, vertices.index(i))
        d.insert(0, i)
        pi.insert(0, i)
        output.append(d)
        output.append(pi)
        top_column.append(i)

    output.insert(0, top_column)

    write_to_csv(output, 'all_outputs')

# Use with caution - very inefficient code - for testing only
def get_graph_csv_task_2(station_data_graph, vertices):
    top_column = ['STARTS ->']
    output = []
    # Double loop so we can run the algorithm for every possible route
    full_run_time_start = time.time()
    for station_outer in vertices: # Use station_outer as start
        # next_column is a count of all inbetween stations for all other stations
        next_column = [station_outer]
        start_time = time.time()
        for station_inner in vertices: # Use station_inner as destination
            # Run Dijkstra's algorithm from the clrs library to find the shortest route to all stations based on user input
            d, pi = dijkstra.dijkstra(station_data_graph, vertices.index(station_outer)) # Start station
            dijkstra_outputs = []
            for i in range(len(vertices)):
                # Create a sensible data structure of the output
                dijkstra_outputs.append({'dest': vertices[i], 'd': d[i], 'pi': ("None" if pi[i] is None else vertices[pi[i]])})

            # Get route by looking for each predecessor in shortest path output
            route = []
            all_stations_added = False
            next_station_to_find = station_inner # End station
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
            # Remove count for start and end stations - we only want the inbetween
            next_column.append(station_count - 2)

        # Add columns to build CSV
        top_column.append(station_outer)
        output.append(next_column)

        # This code is very slow - we want to display to the user that it's working
        end_time = time.time()
        print('Processing done for: ' + station_outer + ' - ' + station_inner + ' | ' + str(len(next_column)) + ' data points | time taken: ' + str(round(end_time - start_time, 3)) + 's')

    full_run_time_end = time.time()
    print('Total time taken: ' + str(round(full_run_time_end - full_run_time_start, 3)) + 's')

    # Insert top row and generate CSV
    output.insert(0, top_column)
    write_to_csv(output, 'all_outputs_stops')

def get_graph_task_3(station_data_graph, vertices):
    top_column = ['STARTS ->']
    output = []
    for station_outer in vertices: # Use station_outer as start
        # next_column is a count of all inbetween stations for all other stations
        next_column = [station_outer]
        start_time = time.time()
        for station_inner in vertices: # Use station_inner as dest
            route, station_count = task_3.task_3_algorithm(station_data_graph, vertices, station_outer, station_inner)

            # Remove count for start and end stations - we only want the inbetween
            next_column.append(station_count - 2)

        # Add columns to build CSV
        top_column.append(station_outer)
        output.append(next_column)

        end_time = time.time()
        print('Processing done for: ' + station_outer + ' - ' + station_inner + ' | ' + str(len(next_column)) + ' data points | time taken: ' + str(round(end_time - start_time, 3)) + 's')

    # Insert top row and generate CSV
    output.insert(0, top_column)
    write_to_csv(output, 'all_outputs_stops')

def get_edge_csv_task_4(underground_graph_mst, underground_graph_mst_edges, vertices):
    # Get list of weighted edges
    edges_with_weights = []
    for mst_edge in underground_graph_mst_edges:
        edge_string = str(underground_graph_mst.find_edge(mst_edge[0], mst_edge[1]))
        edges_with_weights.append([mst_edge[0], int(edge_string.split(' ')[0]), int(edge_string.split('(')[1].rstrip(')'))])

    edges_with_weights_names = []
    for edge in edges_with_weights:
        edges_with_weights_names.append(['NO LINE', vertices[edge[0]], vertices[edge[1]], edge[2]])

    vertices_to_csv = []
    for vert in vertices:
        vertices_to_csv.append(['NO LINE', vert])

    # Produce two files and compile manually so we can import these to run other algorithms
    write_to_csv(vertices_to_csv, 'vertices')
    write_to_csv(edges_with_weights_names, 'task_4_edges')

if __name__ == "__main__":
    # Generate some random data for testing algorithms
    random_edges = []
    i = 0
    while i < 500:
        random_weight = random.randint(1, 5)
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        random_letter_u = alphabet[random.randint(0, 25)]
        random_letter_v = alphabet[random.randint(0, 25)]
        random_edges.append([random_letter_u, random_letter_v, random_weight])
        i += 1

    write_to_csv(random_edges, 'random_data')


