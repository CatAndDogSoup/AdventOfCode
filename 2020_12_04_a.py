# Read file with AdventOfCode day 4 list
with open("2020_12_04_input", "r") as f:
    read_data = f.read()
    # Split data into array
    split_data = read_data.split("\n\n")
    # Remove any empty listings
    split_data = list(filter(None, split_data))
    #split_data = split_data.replace("\n", " ")
    item_field = ""
    item_fields = []
    required_data = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    amount = 0
    #print(split_data)
    for item in split_data:
        item_data = item.replace("\n", " ")
        item_tuple = item_data.split(" ")
        #print(item_tuple)
        for field in item_tuple:
            item_field = field.split(":")[0]
            item_fields.append(item_field)

        result = all(elem in item_fields for elem in required_data)
        if result:
            amount = amount + 1
        print(item_fields)
        item_fields = []
    print(amount)