# Read file with AdventOfCode day 4 list
with open("2020_12_04_list", "r") as f:
    read_data = f.read()
    # Split data into array
    split_data = read_data.split("\n\n")
    # Remove any empty listings
    split_data = list(filter(None, split_data))
    #split_data = split_data.replace("\n", " ")
    item_field = ""
    item_fields = []
    required_data = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    amount = 0
    #print(split_data)
    for item in split_data:
        flattened = item.replace('\n', ' ')
        #print(item)
        item_dict = {}
        for i in flattened.split(' '):
            if i:
                key = i.split(':')[0]
                value = i.split(':')[1]
                item_dict[key]=value
        if required_data.issubset(item_dict.keys()):
            print(item_dict)

        #if result:
            #amount = amount + 1
        #print(item_fields)
        #item_fields = []
    #print(amount)
