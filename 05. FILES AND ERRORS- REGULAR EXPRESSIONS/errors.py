def calc_number(number):
    if number == 0:
        raise ZeroDivisionError('Cannot be zero')
    else:
        return 5/number

num = int(input())

try:
    result = calc_number(num)
except:
    num = int(input())