"""
    Author: Matthew Vallance 001225832
    Purpose: Data imports from London Underground CSV
    Date: 16/10/23
"""
import csv
import unittest

# Get data from CSV and format into appropriate data structure
def get_data():
    # Open and read CSV file
    with open('data/london_underground_data.csv', 'r') as file:
        # Read CSV file
        data = csv.reader(file)

        # Put data into an appropriate data structure
        count = 0
        temp_count = 0
        station_data = []
        station_list = []
        for line in data:
            # print(line)
            # Add connections with times to an array
            # ! INCL TEMPORARY 5 ITEM LIMIT
            if line[2] != '' and temp_count < 4:
                # Format: [str: start station, str: dest. station, int: time between stations]
                station_data.append([line[1], line[2], int(line[3])])
                temp_count += 1

            # Create a list of stations with an id to represent them
            if line[2] == '':
                # Format: [int: id, str: line, str: station]
                station_list.append([int(count), line[0], line[1]])

            count += 1

        return [station_data, station_list]


# TODO: test the correctness of the data
class Test_get_data_method(unittest.TestCase):
    """
    considerations on the testing: (are we handling the following points?)
        1. This data may have inaccuracies or missing information. It's up to you to determine
how to address and report these issues in your study
        2. The dataset excludes durations associated with waiting times at stations and the
process of passengers boarding or alighting.
    """
    def __init__(self, station_data, station_list):
        pass
    
# Run code if called directly
if __name__ == '__main__':
    station_data, station_list = get_data()
    # print(station_data)
    print(station_list)
    """
    ? so the line is not needed? there are many ways to get from one statoin to another by chanignig lines
    e.g. you can take picadilly or victoria line. do you need to show it at the end if you changed lines or the line taht you are using?
    """
    