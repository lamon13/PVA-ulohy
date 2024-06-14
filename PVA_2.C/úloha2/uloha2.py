import math

point1 = []
point2 = []
point3 = []

point1_input = input("point A: ").split()

if len(point1_input) != 2:
    print("wrong input")
    exit()

for i in range(len(point1_input)):
    p = point1_input[i]
    try:
        float(p)
    except ValueError:
        print("wrong input")
        exit()
        
point1 = [float(i) for i in point1_input]

point2_input = input("point B: ").split()

if len(point2_input) != 2:
    print("wrong input")
    exit()

for i in range(len(point2_input)):
    p = point2_input[i]
    try:
        float(p)
    except ValueError:
        print("wrong input")
        exit()
        
point2 = [float(i) for i in point2_input]

point3_input = input("point C: ").split()

if len(point3_input) != 2:
    print("wrong input")
    exit()

for i in range(len(point3_input)):
    p = point3_input[i]
    try:
        float(p)
    except ValueError:
        print("wrong input")
        exit()
        
point3 = [float(i) for i in point3_input]

if point1 == point2 or point1 == point3 or point2 == point3:
    print("Some points are overlapping")
    exit()

def are_points_collinear(p1, p2, p3):
    return p1[0] * (p2[1] - p3[1]) - p1[1] * (p2[0] - p3[0]) + (p2[0] * p3[1]) - (p3[0] * p2[1]) == 0

def find_middle_point(p1, p2, p3):
    if (p1[0] <= p2[0] <= p3[0] or p3[0] <= p2[0] <= p1[0]) and (p1[1] <= p2[1] <= p3[1] or p3[1] <= p2[1] <= p1[1]):
        return "B"
    elif (p2[0] <= p1[0] <= p3[0] or p3[0] <= p1[0] <= p2[0]) and (p2[1] <= p1[1] <= p3[1] or p3[1] <= p1[1] <= p2[1]):
        return "A"
    else:
        return "C"
    
if are_points_collinear(point1, point2, point3):
    print("points are inline")
    print("and the middle point is {find_middle_point(point1, point2, point3)}.")
else:    
    print("points are not inline")
