data = input()
dict = {}
while data != "Over":
    splited_data = data.split(" : ")
    name = splited_data[0]
    number = splited_data[1]

    if number.isdigit():
        dict[name] = number
    else:
        dict[number] = name

    data = input()

for key, value in sorted(dict.items()):
    print(f"{key} -> {value}")
