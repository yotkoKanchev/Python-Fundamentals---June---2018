data = input()
dict = {}

while data.lower() != "end":

    splited_data = data.split(" = ")
    name = splited_data[0]
    number = splited_data[1]

    if number.isdigit():
        dict[name] = int(number)
    else:
        if dict.get(number):
            dict[name] = dict[number]

    data = input()

for key, value in dict.items():
    print(f"{key} === {dict[key]}")