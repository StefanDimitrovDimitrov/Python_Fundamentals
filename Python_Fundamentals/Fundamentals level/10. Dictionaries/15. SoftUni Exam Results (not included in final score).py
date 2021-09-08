students = {}
submissions = {}
while True:
    command = input()

    if command == "exam finished":
        break

    username = command.split("-")[0]
    language = command.split("-")[1]
    if language == "banned":
        del students[username]
        continue
    else:
        points = int(command.split("-")[2])

    if username not in students:
        students[username] = points

        if language not in submissions:
            submissions[language] = 1
        else:
            submissions[language] += 1
    else:
        if students[username] < points:
            students[username]= points
            submissions[language] += 1
        else:
            submissions[language] += 1

students = dict(sorted(students.items(), key=lambda x: (-x[1], x[0])))
submissions = dict(sorted(submissions.items(), key=lambda x: (-x[1], x[0])))

print("Results:")

for k,v in students.items():
    print(f"{k} | {v}")

print("Submissions:")

for k,v in submissions.items():
    print(f"{k} - {v}")