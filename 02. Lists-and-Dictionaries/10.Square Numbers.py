import math
data_list = list(map(int, input().split()))
new_list = []

for item in data_list:
    if item > 0 and math.sqrt(item) == int(math.sqrt(item)):
        new_list.append(item)

new_list.sort(reverse=True)

print(*new_list)