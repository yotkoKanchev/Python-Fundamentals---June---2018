n = int(input())
dict = {}

for i in range(1,n+1):
    data = input()
    stock = data.split(" -> ")
    color = stock[0]
    clothes = stock[1].split(",")

    if color not in dict:
        dict[color] = {}

    for cloth in clothes:
        if cloth not in dict[color]:
            dict[color][cloth] = 1
        else:
            dict[color][cloth] +=1

task_data = input()
asked_color = task_data.split()[0]
asked_cloth = task_data.split()[1]

for key in dict.keys():
    print(f"{key} clothes:")
    for item in dict[key].keys():
        if asked_color == key and asked_cloth == item:
            print(f"* {item} - {dict[key][item]} (found!)")
        else:
            print(f"* {item} - {dict[key][item]}")