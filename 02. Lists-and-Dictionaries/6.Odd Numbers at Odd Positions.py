list_data = list(map(int, input().split(" ")))

for i in range(0, len(list_data)):
    if i % 2 != 0 and list_data[i] % 2 != 0:
        print(f"Index {i} -> {list_data[i]}")

