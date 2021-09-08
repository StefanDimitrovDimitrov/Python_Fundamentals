n = int(input())

students = {}

for i in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []

    students[student_name].append(grade)

students_average_grade = {key: sum(value) / len(value) for (key, value) in students.items() if sum(value) / len(value) >= 4.5 }

# for student, grades in students.items():
#     average = sum(grades) / len(grades)
#
#     if average < 4.5:
#         continue
#
#     students_average_grade[student] = average

students_average_grade = dict(sorted(students_average_grade.items(), key=lambda x: x[1], reverse=True))

for student, avrg in students_average_grade.items():
    print(f"{student} -> {avrg:.2f}")
