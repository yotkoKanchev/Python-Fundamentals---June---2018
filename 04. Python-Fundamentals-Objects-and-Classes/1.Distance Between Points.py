import math

class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y

def calculate_distance(a,b):
    c = math.sqrt(a**2 + b**2)
    return c

data = list(map(float, input().split()))
data1 = list(map(float, input().split()))

x1 = data[0]
y1 = data[1]
x2 = data1[0]
y2 = data1[1]

first_point = Point(x1,y1)
second_point = Point(x2,y2)

side_a = abs(first_point.x - second_point.x)
side_b = abs(first_point.y - second_point.y)

side_c = calculate_distance(side_a,side_b)

print(f"{side_c:.3f}")