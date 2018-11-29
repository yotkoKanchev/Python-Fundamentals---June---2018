base = float(input())
heigh = float(input())

def triangle_area(a,h):
    area = a*h/2
    return area

print(f"{triangle_area(base,heigh):.12g}")