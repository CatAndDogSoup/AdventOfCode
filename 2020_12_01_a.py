with open("2020_12_01_list", "r") as f:
    read_data = f.read()
    split_data = read_data.split("\n")
    split_data = list(filter(None, split_data))
    for i in range(0, len(split_data)):
        split_data[i] = int(split_data[i])
    #print(split_data)
    for i in split_data:
        for j in split_data:
            #print(i + j)
            k = i+j
            if k == 2020:
                print(i, '  ', j)
