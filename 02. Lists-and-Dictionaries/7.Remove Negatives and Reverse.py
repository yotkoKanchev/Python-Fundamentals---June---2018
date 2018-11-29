data_list = list(map(int, input().split(" ")))

new_list = []

for item in data_list:
    if item > 0:
        new_list.append(item)

if new_list == []:
    print("empty")
else:
    print(*reversed(new_list))

