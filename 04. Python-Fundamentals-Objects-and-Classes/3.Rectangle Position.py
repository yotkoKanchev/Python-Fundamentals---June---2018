class Rectangle:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

rec_data1 = list(map(int, input().split()))
rec_data2 = list(map(int, input().split()))

left1 = rec_data1[0]
top1 = rec_data1[1]
width1 = rec_data1[2]
height1 = rec_data1[3]

left2 = rec_data2[0]
top2 = rec_data2[1]
width2 = rec_data2[2]
height2 = rec_data2[3]

rectangle1 = Rectangle(left1, top1, width1, height1)
rectangle2 = Rectangle(left2, top2, width2, height2)

if rectangle1.left >= rectangle2.left and rectangle1.top >= rectangle2.top \
        and rectangle1.width + rectangle1.left <= rectangle2.width + rectangle2.left \
        and rectangle1.height + rectangle1.top <= rectangle2.height + rectangle2.top:
    print(f"Inside  ")
else:
    print(f"Not inside")