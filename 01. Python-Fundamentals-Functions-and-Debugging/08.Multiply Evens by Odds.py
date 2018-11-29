data = int(input())

def mul_even_odd(num):
    odd_sum = 0
    even_sum = 0
    num = str(num)

    for i in num:
        if i == "-":
            continue
        elif int(i) % 2 == 0:
            even_sum += int(i)
        else:
            odd_sum += int(i)

    result = even_sum*odd_sum
    return result

print(mul_even_odd(data))