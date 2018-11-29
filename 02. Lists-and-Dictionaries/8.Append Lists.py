data_list = input().split("|")

data_list.reverse()
result_list = []

for item in data_list:
    result_list.extend(item.split())

print(*(result_list))
