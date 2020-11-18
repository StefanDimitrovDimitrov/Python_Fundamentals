import math

number_people = int(input())
capacity = int(input())

full_courses = math.ceil(number_people /capacity)

print(f'{full_courses}')