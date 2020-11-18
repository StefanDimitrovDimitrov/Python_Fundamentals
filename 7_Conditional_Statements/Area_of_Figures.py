from math import pi

type = input()
area = 0

if type == "square":
    side_a = float(input())
    area = side_a* side_a

elif type == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b

elif type == "circle":
    radius = float(input())
    area = pi * radius * radius

elif type == "triangle":
    length = float(input())
    height = float(input())
    area = length * height / 2

print(f"{area: .3f}")

