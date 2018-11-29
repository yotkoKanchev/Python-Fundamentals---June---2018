import math
data = input()
dict = {}
while data != "Aggregate":

    crab_data = data.split(" ")
    name = crab_data[0]
    size = int(crab_data[1])


    if name not in dict:
        dict[name] = []
        dict[name].append(size)
    else:
        if size not in dict[name]:
            dict[name].append(size)

    data = input()
for key, value in dict.items():
    print(f"{key} -> {', '.join(map(str, value))} ",end="")
    average = sum(value) - sum(value)/ len(dict[key])
    print(f"({math.ceil(average)})")