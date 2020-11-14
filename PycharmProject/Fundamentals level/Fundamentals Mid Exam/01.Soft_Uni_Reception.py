first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
visitors = int(input())

capacity = first_employee + second_employee + third_employee

hours = 0

while visitors > 0:

    hours += 1
    visitors -= capacity

    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")