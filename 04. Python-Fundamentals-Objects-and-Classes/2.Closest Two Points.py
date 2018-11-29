from math import sqrt

class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def calc_distance(self,p2):
        a = p2.x - self.x
        b = p2.y - self.y
        return sqrt(a**2 + b**2)

n = int(input())
list_points = []

for i in range(1, n+1):

    data = list(map(int, input().split()))
    x1 = data[0]
    y1 = data[1]
    point = Point(x1,y1)

    list_points.append(point)

min_distance = list_points[0].calc_distance(list_points[1])
first_point = list_points[0]
second_point = list_points[1]

for i in list_points:
    for j in list_points:
        current_distance = i.calc_distance(j)
        if list_points.index(i) != list_points.index(j) and current_distance < min_distance:
            min_distance = current_distance
            first_point = i
            second_point = j

print(f"{min_distance:.3f}")
print(f"({first_point.x}, {first_point.y})")
print(f"({second_point.x}, {second_point.y})")

