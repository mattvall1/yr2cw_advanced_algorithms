"""
    Author: Matthew Vallance 001225832
    Purpose: Data imports from London Underground CSV
    Date: 16/10/23
"""
import csv

# Return an array of the nodes in the graph
def remove_duplicate_stations(station_list) -> list:
    return list(set(station_list))

# Get data from CSV and format into appropriate data structure - using above functions
def get_data():
    # Open and read CSV file
    # with open('data/small_data.csv', 'r') as file: # Uncomment for testing on one line - Bakerloo
    # with open('data/medium_data.csv', 'r') as file: # Uncomment for testing on two lines - Bakerloo + Central
    # with open('data/large_data.csv', 'r') as file: # Uncomment for testing on three lines - Bakerloo + Central + Circle
    with open('data/london_underground_data.csv', 'r') as file:
        # Read CSV file
        data = csv.reader(file)

        # Put data into an appropriate data structure
        station_data = []  # edges
        station_list = []  # nodes in the graph
        for line in data:
            # Add connections with times to an array
            if line[2] != '':
                # Format: [str: line, str: start station, str: dest. station, int: time between stations]
                # TODO: Explain apostrophe removal in report
                station_data.append(
                    [line[1].rstrip().replace('\'', ''), line[2].rstrip().replace('\'', ''), int(line[3])])

            # Create a list of stations
            if line[2] == '':
                station_list.append(line[1].rstrip().replace('\'', ''))

    # Remove duplicate stations
    station_list_no_duplicates = remove_duplicate_stations(station_list)

    return [station_list_no_duplicates, station_data]
