num_list = list(map(int, input().split(" ")))
p = int(input())
result_list = []
for num in num_list:
    new_num = num*p
    result_list.append(new_num)

print(*result_list)