# Read file with AdventOfCode day 3 list
with open("2020_12_03_list", "r") as f:
    read_data = f.read()
    # Split data into array
    split_data = read_data.split("\n")
    # Remove any empty listings
    split_data = list(filter(None, split_data))
    #print(split_data)
    width = len(split_data[0])
    horizontal = 0
    amount = 0
    print(len(split_data))
    for i in range(0, len(split_data)):
        horizontal = horizontal + 3
        if horizontal >= width:
            horizontal = horizontal - width
        #print(horizontal)
        #print(split_data[i][horizontal])
        if split_data[i][horizontal] == "#":
            print(str(split_data[i][horizontal]).replace('#','X'))
            amount = amount + 1
            #print(split_data[i])
        else:
            print(split_data[i])
    print(amount)
