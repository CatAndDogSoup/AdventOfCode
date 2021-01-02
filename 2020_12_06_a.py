a = set([1,1,1,2,2,3])
print(a)

# Read file with AdventOfCode day 6 input
with open("2020_12_06_input", "r") as f:
    read_data = f.read()
    # Split data into array
    split_data = read_data.split("\n\n")
    # Remove any empty listings
    split_data = list(filter(None, split_data))
    print(split_data)
    # Variables
    cleaned_data = []
    addition = 0
    for i in split_data:
        i = i.replace('\n','')
        cleaned_data.append(i)
    group_answer = [set(temp_group.replace("\n","")) for temp_group in split_data]
    print(group_answer)
    for i in group_answer:
        addition = len(i) + addition
    print(addition)