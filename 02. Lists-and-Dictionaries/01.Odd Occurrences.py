data = input()
lowered_data = data.lower().split(" ")
dict_input = {}

for item in lowered_data:
    if item in dict_input:
        dict_input[item] += 1
    else:
        dict_input[item] = 1

string_output = ''
for item in dict_input:
    if dict_input[item] % 2 != 0:
        string_output += item + ", "

print(string_output.strip(", "))