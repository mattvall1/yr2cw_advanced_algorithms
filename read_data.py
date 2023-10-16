import csv

# Get data from CSV and format into appropriate data structure
def get_data():
    # Open and read CSV file
    with open('data/london_underground_data.csv', 'r') as file:
        # Read CSV file
        data = csv.reader(file)

        # Put data into an appropriate data structure - USE crls_library HERE
        for line in data:
            print(line)

