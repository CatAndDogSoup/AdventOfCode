# Read file with AdventOfCode day 5 input
import math
with open("2020_12_05_input", "r") as f:
    read_data = f.read()
    # Split data into array
    split_data = read_data.split("\n")
    # Remove any empty listings
    split_data = list(filter(None, split_data))
    #split_data = split_data.replace("\n", " ")
    highest_seat = 0
    highest_row = 127
    lowest_row = 0
    highest_column = 7
    lowest_column = 0
    results = []
    #print(split_data)
    def binary_search(input_char,num):
        global highest_row
        global lowest_row
        global highest_column
        global lowest_column

        if input_char == "F" and not num:
            highest_row = math.floor(highest_row / 2)
        elif input_char == "B" and not num:
            lowest_row = math.floor((lowest_row + highest_row) /2)
        if input_char == "L" and num:
            highest_column = math.floor(highest_column / 2)
        elif input_char == "R" and num:
            lowest_column = math.floor((lowest_column + highest_column) / 2)

        return highest_row, lowest_row, highest_column, lowest_column

    for row in split_data:
        for i in row[0:6]:
            result = binary_search(i,0)
        for i in row[6:9]:
            result = binary_search(i,1)
            print(result)

        results.append((result[0] * 8) + max(result[2],result[3]))
        highest_row = 127
        lowest_row = 0
        highest_column = 7
        lowest_column = 0

    print(results)
    print(max(results))