"""
    Author: Matthew Vallance 001225832
    Purpose: Data imports from London Underground CSV
    Date: 16/10/23
"""
import csv

# Return an array of the nodes in the graph
def remove_duplicate_stations(station_list) -> list:
    return list(set(station_list))

# return the nodes with an index 
# ? is there any way on how you wanna index all the nodes?, e.g. cutty sark must be index 5? ig it doesnt matter 
def add_id_to_stations(station_list_no_duplicates:list) -> list:
    """
    input -> nodes in the graph
    output -> indexed station
    """
    station_list_with_ids = []
    count = 0
    for station in station_list_no_duplicates:
        # ? why int(count), count is already an integer
        # station_list_with_ids.append([int(count), station.rstrip().replace('\'', '')])
        station_list_with_ids.append([count, station.rstrip().replace('\'', '')])
        count += 1
    return station_list_with_ids

# Get data from CSV and format into appropriate data structure - using above functions
def get_data():
    # Open and read CSV file
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
                station_list.append(line[1].rstrip())

    # Remove duplicate stations
    station_list_no_duplicates = remove_duplicate_stations(station_list)  # return the nodes in the graph

    # Add IDs to stations
    station_list_with_ids = add_id_to_stations(station_list_no_duplicates)


    # Assign the station IDs to each connection, to create edges to insert into the graph
    station_edges = []
    all_possible_edges = set()
    for start, stop, time in station_data:
        all_possible_edges.add((start, stop, time))
        all_possible_edges.add((stop, start, time))
    all_possible_edges = list(all_possible_edges)
    print(all_possible_edges)
    """
    but you have to do it with indexes so its tricky if you use the variable station_list_with_ids with a list 
    why not a dict() and then you map the name with its index?

    so to put all the stations with its index lets have a variable called staions which is all the nodes in the graph
    assumptions: a station only appear once and only once (cannot be: ["cutty", "cutty"])

    stations = []
    map_station_idx = defaultdict(int)
    count = 0

    # put values on map
    for s in station:
        map_station_idx[s] = count  # assign -> "cutty" = 0         then        "greenwich" = 1     etc...
        count += 1

    # now that we have the values indexed, we can map the any staiton in O(1) time 
    # lets use the undirected graph code that i wrote above
    station_edges = []  # ['Bethnal Green', 'Liverpool Street', '3']
    all_possible_edges = set()
    for start, stop, time in station_data:
        all_possible_edges.add((map_station_idx[start], map_station_idx[stop], time))
        all_possible_edges.add((map_station_idx[stop], map_station_idx[start], time))
    all_possible_edges = list(all_possible_edges)

    # now all_possible_edges is your final result 
    # in your code you are calling it station_edges
    # i kinda bruted forced the solution using set, not sure if there is a better implementation, if you find it out please let me know :)
    """

    # station_edges = []
    # for connection in station_data:
    #     # Get station edges to insert into array
    #     start = 0
    #     dest = 0
    #     for station in station_list_with_ids:
    #         # Start
    #         if connection[0] == station[1]:
    #             start = station[0]
    #         # Destination
    #         if connection[1] == station[1]:
    #             dest = station[0]
    #
    #     # Make sure each edge is in the same order - this is so we can get the smallest weight easier
    #     if start < dest:
    #         station_edges.append([start, dest, int(connection[2])])
    #     else:
    #         station_edges.append([dest, start, int(connection[2])])
    #
    # # Remove duplicate edges
    # station_edges = [list(x) for x in set(tuple(x) for x in station_edges)]
    # station_edges = sorted(station_edges)
    # station_edges_duplicates = []
    # for i in range(0, len(station_edges)):
    #     # Get a list of the duplicated edges with the higher weight
    #     if station_edges[i][0] == station_edges[i - 1][0] and station_edges[i][1] == station_edges[i - 1][1]:
    #         station_edges_duplicates.append(station_edges[i])
    # for station_edge_duplicate in station_edges_duplicates:
    #     station_edges.remove(station_edge_duplicate)
    # print(station_edges)

    return [station_data, all_possible_edges, station_list_with_ids]