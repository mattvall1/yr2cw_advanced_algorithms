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
                station_data.append([line[0], line[1], line[2], int(line[3])])

            # Create a list of stations
            # THINK ABOUT DUPLICATED EDGWARE ROAD HERE
            if line[2] == '':
                station_list.append(line[1].rstrip())

    # Remove duplicate stations and add ids
    station_list_clean = []
    count = 0
    for station in np.unique(station_list):
        station_list_clean.append([int(count), station])
        count += 1

    return [station_data, station_list_clean]
