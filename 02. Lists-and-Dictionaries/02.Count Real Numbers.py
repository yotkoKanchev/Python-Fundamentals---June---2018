data = input()
splited_data = list(map(float, data.split()))

dict_input = {}
for item in splited_data:
    if item in dict_input:
        dict_input[item] += 1
    else:
        dict_input[item] = 1

for item in sorted(dict_input.keys()):
    print(f"{item} -> {dict_input[item]} times")