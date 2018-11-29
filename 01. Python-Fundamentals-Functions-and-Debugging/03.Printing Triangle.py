data = int(input())

def triangle_print(num):
    for i in range(1, num+1):
        for j in range(1, i+1):
            print(f"{j} ", end = "")
        print()
    for i in range(num-1,1-1,-1):
        for j in range(1,i+1):
            print(f"{j} ", end="")
        print()
triangle_print(data)