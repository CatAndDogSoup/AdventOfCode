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
    #x_pos = 0
    x_move = 3
    y_move = 1
    # amount for the final amount of trees hit
    amount = 0
    # loop over every line in split_data
    def dank_trees(x_move, y_move):
        x_pos  = 0
        amount = 0
        for i in range(0, len(split_data), y_move):
            if split_data[i][x_pos] == "#":
                amount = amount + 1
            x_pos = x_pos + x_move
            # wrap x_pos around
            if x_pos >= width:
                x_pos = x_pos - width
        return amount

    print(dank_trees(1, 1) * dank_trees(3, 1) * dank_trees(5, 1) * dank_trees(7, 1) * dank_trees(1, 2))
    #print(amount)