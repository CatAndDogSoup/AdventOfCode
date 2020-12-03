# Read file with AdventOfCode day 2 list
with open("2020_12_02_list", "r") as f:
    read_data = f.read()
    # Split data into array
    split_data = read_data.split("\n")
    # Remove any empty listings
    split_data = list(filter(None, split_data))
    amount = 0
    for item in split_data:
        item_array = tuple(item.split(" "))
        #print(item_array)
        item_minmax = item_array[0].split("-")
        item_min = item_minmax[0]
        item_max = item_minmax[1]
        #print(item_min)
        #print(item_max)
        item_letter = item_array[1].replace(':','')
        item_password = item_array[2]
        #print(item_letter)
        #print(item_password)
        #item_letter = item_letter
        if item_password.count(item_letter) >= int(item_min) and item_password.count(item_letter) <= int(item_max):
            print(item)
            amount = amount + 1
    print(amount)