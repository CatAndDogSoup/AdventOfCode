# Read file with AdventOfCode day 4 list
import re
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
    ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
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
            #print(item_dict["pid"])
            if 1920 <= int(item_dict["byr"]) <= 2002:
                if 2010 <= int(item_dict["iyr"]) <= 2020:
                    if 2020 <= int(item_dict["eyr"]) <= 2030:
                        if "#" in item_dict["hcl"] and len(item_dict["hcl"]) == 7 and re.compile(r'[^a-f0-9]').search:
                            if item_dict["ecl"] in ecl:
                                if len(item_dict["pid"]) == 9:
                                    if "in" in item_dict["hgt"]:
                                        #print("poggies")
                                        amount = amount + 1
                                    if "cm" in item_dict["hgt"]:
                                        #print("poggies")
                                        amount = amount + 1

                        #print(item_dict)


    print(amount)
