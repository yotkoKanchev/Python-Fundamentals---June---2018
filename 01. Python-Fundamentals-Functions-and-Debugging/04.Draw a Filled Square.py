data = int(input())

def top_botom(num):
    print("-"*2*num)

def middle(num):
    for i in range(1, num-1):
        print("-" + "\/"*(num-1) + "-")

top_botom(data)
middle(data)
top_botom(data)