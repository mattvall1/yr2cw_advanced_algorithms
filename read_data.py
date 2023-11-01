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
                station_data.append([line[1].rstrip(), line[2].rstrip(), int(line[3])])

            # Create a list of stations
            # THINK ABOUT DUPLICATED EDGWARE ROAD HERE
            if line[2] == '':
                station_list.append(line[1].rstrip())

    # Remove duplicate stations and add ids
    station_list_clean = []
    count = 0
    for station in np.unique(station_list):
        station_list_clean.append([int(count), station.rstrip()])
        count += 1

    # Assign IDs to each station, to create edges to insert into the graph
    station_edges = []
    for connection in station_data:
        # Get station edges to insert into array
        start = 0
        dest = 0
        for station in station_list_clean:
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
    

    return [station_data, station_edges, station_list_clean]
