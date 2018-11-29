data_list = input()

data_dict = {}

for item in data_list:
    if item in data_dict:
        data_dict[item] += 1
    else:
        data_dict[item] = 1

for item in data_dict:
    print(f"{item} -> {data_dict[item]}")
