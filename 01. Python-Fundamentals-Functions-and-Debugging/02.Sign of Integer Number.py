data = int(input())

def sign_of_integer(num):
    result = ""
    if num > 0:
        result = 'positive'
    elif num < 0:
        result = "negative"
    else:
        result = "zero"
    print(f"The number {num} is {result}.")
sign_of_integer(data)

