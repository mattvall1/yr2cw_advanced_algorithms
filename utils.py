"""
    Author: Matthew Vallance 001225832
    Purpose: Utils file for cleaner code
    Date: 15/11/23
"""
import data_processing


# Check validity of user inputs - return an error message
def validity_check(vertices, start, dest):
    if start == dest:
        print('The start and destination stations cannot be the same. Please check your inputs.')
        return False
    elif start not in vertices and dest not in vertices:
        print('The start and destination stations do not exist or are misspelled. Please check your inputs.')
        return False
    elif start not in vertices:
        print('The start station does not exist or is misspelled. Please check your inputs.')
        return False
    elif dest not in vertices:
        print('The destination station does not exist or is misspelled. Please check your inputs.')
        return False
    else:
        # If we find no issues, return true
        return True


# Reformat strings for consistency and validity checking
def reformat_inputs(start, dest):
    # Remove leading and trailing whitespace and add capitalization of all names in strings
    return [start.strip().title(), dest.strip().title()]


# Get inputs from user
def get_stations_from_user(vertices):
    valid_inputs = False
    # While loop to create a checking system for inputs
    while not valid_inputs:
        start_station = input('Input starting station: ')
        dest_station = input('Input destination station: ')
        start_station, dest_station = reformat_inputs(start_station, dest_station)
        if validity_check(vertices, start_station, dest_station):
            valid_inputs = True

    return start_station, dest_station


def return_data():
    # Get graph and vertices
    underground_graph, underground_vertices = data_processing.get_data()

    # Get station inputs from the user
    start_station, dest_station = get_stations_from_user(underground_vertices)

    # Return all data
    return underground_graph, underground_vertices, start_station, dest_station
