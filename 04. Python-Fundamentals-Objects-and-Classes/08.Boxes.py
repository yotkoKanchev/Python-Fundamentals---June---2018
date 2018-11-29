import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self,other_point):
        x = abs(self.x - other_point.x)
        y = abs(self.y - other_point.y)
        return math.sqrt(x ** 2 + y ** 2)

class Box:
    def __init__(self,upper_l_p, upper_r_p, bottom_l_p, bottom_r_p):
        self.upper_l_p = upper_l_p
        self.upper_r_p = upper_r_p
        self.bottom_l_p = bottom_l_p
        self.bottom_r_p = bottom_r_p
        self.width = Point.calculate_distance(self.upper_l_p, self.upper_r_p)
        self.height = Point.calculate_distance(self.upper_l_p, self.bottom_l_p)
        self.perimeter = self.width*2 + self.height*2
        self.area = self.width * self.height

data = input()

list_boxes = []

while data != "End":
    u_l = data.split(" | ")[0]
    u_r = data.split(" | ")[1]
    b_l = data.split(" | ")[2]
    b_r = data.split(" | ")[3]

    u_l_p = Point(int(u_l.split(":")[0]), int(u_l.split(":")[1]))
    u_r_p = Point(int(u_r.split(":")[0]), int(u_r.split(":")[1]))
    b_l_p = Point(int(b_l.split(":")[0]), int(b_l.split(":")[1]))
    b_r_p = Point(int(b_r.split(":")[0]), int(b_r.split(":")[1]))

    my_box = Box(u_l_p, u_r_p, b_l_p, b_r_p)
    list_boxes.append(my_box)

    data = input()

for box in list_boxes:
    print(f"Box: {int(box.width)}, {int(box.height)}")
    print(f"Perimeter: {int(box.perimeter)}")
    print(f"Area: {int(box.area)}")