data = input()

dict = {}
while data != "filter base":

    base = data .split(" -> ")
    name = base[0]
    parameter = base[1]
    if name not in dict:
        dict[name] = []

    dict[name].append(parameter)

    data = input()

case = input()

for item in dict[name]:
    if case == "Salary":
        if "." in item:
            for key,value in dict.items():
                print(f"Name: {key}")
                print(f"Salary: {value[-1]}")
                print(f"====================")

    elif case == "Age":
        if float(item) - int(item) == 0:
            for key,value in dict.items():
                print(f"Name: {key}")
                print(f"Age: {value[1]}")
                print(f"====================")

    else:
        for key, value in dict.items():
            print(f"Name: {key}")
            print(f"Position: {value[0]}")
            print(f"====================")
