# Read file with AdventOfCode day 1 list
with open("2020_12_01_list", "r") as f:
    read_data = f.read()
    # Split data into array
    split_data = read_data.split("\n")
    # Remove any empty listings
    split_data = list(filter(None, split_data))
    # Convert all array items to ints
    for i in range(0, len(split_data)):
        split_data[i] = int(split_data[i])
    # Run through each item (j) for every item (i) and compares if they add up to 2020
    # and prints the result if it does
    for i in split_data:
        for j in split_data:
            k = i+j
            if k == 2020:
                print(i, '  ', j)