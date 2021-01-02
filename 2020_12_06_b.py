# Read file with AdventOfCode day 6 input
import re
with open("2020_12_06_input", "r") as f:
    read_data = f.read()
    # Split data into array
    split_data = read_data.split("\n\n")
    # Remove any empty listings
    split_data = list(filter(None, split_data))
    # Variables
    cleaned_data = []
    amount = 0
    group_answer = []
    cur_answer = []
    prev_answer = []
    num_people_group = 0
    alphabet = ["abcdefghijklmnopqrstuvwxyz"]
    for group in split_data:
        group = group.splitlines()
        cleaned_data.append(group)
    #print(cleaned_data)

    #group_answer = [set(temp_group.replace("\n","")) for temp_group in split_data]
    for group in cleaned_data:
        for character in group:
            print(character)
            print(len(group))
            if group.count(character) == len(group):
                amount = amount + 1

        #print(len(group))

    #for i in group_answer:
        #addition = len(i) + addition
    #print(addition)
    print(amount)