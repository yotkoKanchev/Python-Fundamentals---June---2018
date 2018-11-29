list_data = input().split(" ")

last_letter = list_data.pop()

list_data.insert(0,last_letter)

print(*list_data)