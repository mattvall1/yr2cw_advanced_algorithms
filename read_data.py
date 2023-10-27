"""
    Author: Matthew Vallance 001225832
    Purpose: Data imports from London Underground CSV
    Date: 16/10/23
"""
import csv


# Get data from CSV and format into appropriate data structure
def get_data():
    # Open and read CSV file
    with open('data/london_underground_data.csv', 'r') as file:
        # Read CSV file
        data = csv.reader(file)

        # Put data into an appropriate data structure
        count = 0
        station_data = []
        station_list = []
        for line in data:
            # Add connections with times to an array
            if line[2] != '':
                # Format: [str: start station, str: dest. station, int: time between stations]
                station_data.append([line[0], line[1], line[2], int(line[3])])

            # Create a list of stations with an id to represent them
            if line[2] == '':
                # Format: [int: id, str: line, str: station]
                station_list.append([int(count), line[0].replace('\ufeff', ''), line[1]])
                count += 1

        return [station_data, station_list]
