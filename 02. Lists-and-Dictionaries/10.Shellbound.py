data = input()

dict = {}

while data != "Aggregate":

    splited_data = data.split()
    city = splited_data[0]
    size = int(splited_data[1])

    if city not in dict:
        dict[city] = []
        dict[city].append(size)
    else:
        if size not in dict[city]:
            dict[city].append(size)
    data = input()
import math
for key in dict.keys():
    print(f"{key} -> {', '.join(map(str, dict[key]))}", end="")
    average = math.ceil(sum(dict[key]) - sum(dict[key]) / len(dict[key]))
    print(f" ({average})")
