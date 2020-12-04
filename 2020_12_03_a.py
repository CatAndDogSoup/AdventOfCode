# Read file with AdventOfCode day 3 list
with open("2020_12_03_list", "r") as f:
    read_data = f.read()
    # Split data into array
    split_data = read_data.split("\n")
    # Remove any empty listings
    split_data = list(filter(None, split_data))
    # width for the line width
    width = len(split_data[0])
    # x_pos for the current horizontal position
    x_pos = 0
    x_move = 3
    y_move = 1
    # amount for the final amount of trees hit
    amount = 0
    # loop over every line in split_data
    for i in range(0, len(split_data), y_move):
        # up x_pos for every iteration

        if split_data[i][x_pos] == "#":
            print(split_data[i][:x_pos] + "X" + split_data[i][x_pos + 1:] + " | " + str(x_pos) + "\t| " + str(i))
            amount = amount + 1
        else:
            print(split_data[i])
        x_pos = x_pos + x_move
        # wrap x_pos around
        if x_pos >= width:
            x_pos = x_pos - width
    print(amount)
