list_data = list(map(int, input().split(" ")))
counter = 0
for i in list_data:
    if i %2 != 0:
        counter+=1
print(counter)