# Read file with AdventOfCode day 2 list
with open("2020_12_02_list", "r") as f:
    read_data = f.read()
    # Split data into array
    split_data = read_data.split("\n")
    # Remove any empty listings
    split_data = list(filter(None, split_data))
    amount = 0
    #loop over every item in #split_data
    for item in split_data:
        #split item into item_array based on spaces
        item_array = tuple(item.split(" "))
        #split item_array part 0 (min-max) into seperate variables
        item_minmax = item_array[0].split("-")
        item_min = item_minmax[0]
        item_max = item_minmax[1]
        #sets the item_letter as the item to check how many of each are in the password
        item_letter = item_array[1].replace(':','')
        #sets item_password as the password
        item_password = item_array[2]
        #checks if the item_letter is in the password between item_min and item_max amounts
        if item_password.count(item_letter) >= int(item_min) and item_password.count(item_letter) <= int(item_max):
            print(item)
            #up the amount variable for every occurance
            amount = amount + 1
    print(amount)