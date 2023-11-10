"""
    Author: Matthew Vallance 001225832
    Purpose: Simple script to put data into a CSV for comparison externally
    Date: 26/10/23
"""
import csv

from clrs_library_slim import dijkstra


def write_to_csv(data, filename='testing_data'):
    with open("testing/csv_output/"+filename+".csv", "w") as file_to_write:
        # Create writer to write row
        writer = csv.writer(file_to_write)
        # Write each row of data to the CSV file
        for row in data:
            writer.writerow(row)
        print('Generated ' + filename + '.csv')


def get_graph_csv(station_data_graph, station_list):
    # TESTING CODE TO OUTPUT CSV OF ALL EDGES + STATIONS
    output = []
    top_column = ['']
    for i in station_list:
        d, pi = dijkstra.dijkstra(station_data_graph, i[0])
        d.insert(0, i[1])
        pi.insert(0, i[1])
        output.append(d)
        output.append(pi)
        top_column.append(i[1])

    output.insert(0, top_column)

    write_to_csv(output, 'all_outputs')