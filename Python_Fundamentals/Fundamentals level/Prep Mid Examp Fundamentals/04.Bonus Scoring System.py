import math

count_of_the_students = int(input())
count_of_the_lectures = int(input())
initial_bonus = int(input())

total_bonus = 0
max_bonus = 0
num_lectures = 0

for i in range(count_of_the_students):
    attendances_of_each_student = int(input())

    if count_of_the_lectures != 0:

            total_bonus = (attendances_of_each_student / count_of_the_lectures) * (5 + initial_bonus)

            if total_bonus >= max_bonus:
                max_bonus = total_bonus
                num_lectures = attendances_of_each_student

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {num_lectures} lectures.")