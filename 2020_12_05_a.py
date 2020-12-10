# Read file with AdventOfCode day 5 input
import math
with open("2020_12_05_input", "r") as f:
    read_data = f.read()
    # Split data into array
    split_data = read_data.split("\n")
    # Remove any empty listings
    split_data = list(filter(None, split_data))
    # Variables
    highest_seat = 0
    highest_row = 127
    lowest_row = 0
    highest_column = 7
    lowest_column = 0
    results = []
    def binary_search(input_char):
        # Import variables
        global highest_row
        global lowest_row
        global highest_column
        global lowest_column
        # does shit
        if input_char == "F":
            highest_row = math.floor((lowest_row + highest_row) / 2)
        if input_char == "B":
            lowest_row = math.floor((lowest_row + highest_row) / 2)
        if input_char == "L":
            highest_column = math.ceil(highest_column / 2)
        if input_char == "R":
            lowest_column = math.floor((lowest_column + highest_column) / 2)

        # Return result
        return highest_row, lowest_row, highest_column, lowest_column

    # Run over every row
    for row in split_data:
        # Run over every character in that row
        for i in row:
            # Set the result based on binary_search
            result = binary_search(i)
        # appends the result to the results list
        results.append((max(result[0:1]) * 8) + max(result[2],result[3]))
        # resets the variables
        highest_row = 127
        lowest_row = 0
        highest_column = 7
        lowest_column = 0
    # prints result
    print(max(results))