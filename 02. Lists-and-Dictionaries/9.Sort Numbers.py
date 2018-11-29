list_data = list(map(int, input().split(" ")))

list_data.sort()

print(" <= ".join(map(str, list_data)))