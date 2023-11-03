"""
    Author: Matthew Vallance 001225832
    Purpose: Data imports from London Underground CSV
    Date: 16/10/23
"""
import csv
import numpy as np


# Get data from CSV and format into appropriate data structure
def get_data():
    # Open and read CSV file
    with open('data/london_underground_data.csv', 'r') as file:
        # Read CSV file
        data = csv.reader(file)

        # Put data into an appropriate data structure
        station_data = []
        station_list = []
        for line in data:
            # Add connections with times to an array
            if line[2] != '':
                # Format: [str: line, str: start station, str: dest. station, int: time between stations]
                # TODO: Explain apostrophe removal in report
                station_data.append([line[1].rstrip().replace('\'', ''), line[2].rstrip().replace('\'', ''), int(line[3])])

            # Create a list of stations
            if line[2] == '':
                station_list.append(line[1].rstrip())

    # Remove duplicate stations
    count = 0
    seen_stations = set()
    station_list_no_duplicates = []
    for station in station_list:
        if station not in seen_stations:
            station_list_no_duplicates.append(station)
            seen_stations.add(station)

    # Add IDs to stations
    station_list_with_ids = []
    for station in station_list_no_duplicates:
        station_list_with_ids.append([int(count), station.rstrip().replace('\'', '')])
        count += 1

    # Assign the station IDs to each connection, to create edges to insert into the graph
    station_edges = []
    for connection in station_data:
        # Get station edges to insert into array
        start = 0
        dest = 0
        for station in station_list_with_ids:
            # Start
            if connection[0] == station[1]:
                start = station[0]
            # Destination
            if connection[1] == station[1]:
                dest = station[0]

        # Make sure each edge is in the same order - this is so we can get the smallest weight easier
        if start < dest:
            station_edges.append([start, dest, int(connection[2])])
        else:
            station_edges.append([dest, start, int(connection[2])])

    # Remove duplicate edges
    station_edges = [list(x) for x in set(tuple(x) for x in station_edges)]
    station_edges = sorted(station_edges)
    station_edges_duplicates = []
    for i in range(0, len(station_edges)):
        # Get a list of the duplicated edges with the higher weight
        if station_edges[i][0] == station_edges[i - 1][0] and station_edges[i][1] == station_edges[i - 1][1]:
            station_edges_duplicates.append(station_edges[i])
    for station_edge_duplicate in station_edges_duplicates:
        station_edges.remove(station_edge_duplicate)

    csvwrite.write_to_csv(station_data, 'station_data')

    return [station_data, station_edges, station_list_with_ids]