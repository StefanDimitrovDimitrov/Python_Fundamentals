from _collections import defaultdict

line = defaultdict(int)
users_contests_points = defaultdict()
temp = []
names = set()
temp_dict = defaultdict(int)
total_points = 0
final_dic = {}



while True:
    command = input()

    if command == "end of contests":
        break

    contest, password_of_contest = command.split(":")

    line[contest] = password_of_contest

while True:
    students = input()

    if students == "end of submissions":
        break
    name_of_student = students.split("=>")[2]
    names.add(name_of_student)
    temp.append(students)

 # users[username] = {contest_name:int(points)}
for n in names:
    for student in temp:
        contest_name,password,username,points = student.split("=>")

        if username == n:
            for l in line.keys():
                if contest_name == l and password == line[l]:
                    if n not in users_contests_points:
                        users_contests_points[n] = {contest_name:int(points)}
                    else:
                        if contest_name in users_contests_points[n].keys():
                            if int(points) > users_contests_points[n][contest_name]:
                                users_contests_points[n].update({contest_name:int(points)})
                        else:
                            users_contests_points[n].update({contest_name:int(points)})

for k in users_contests_points.keys():
    for t,v in users_contests_points[k].items():
        total_points += int(v)
        if k not in final_dic:
            final_dic.update({k:int(v)})
        else:
            final_dic[k] += int(v)


winer = max(final_dic, key=final_dic.get)


for k in users_contests_points.keys():
    for t,v in users_contests_points[k].items():
        users_contests_points[k] = dict(sorted(users_contests_points[k].items(), key= lambda x: (-x[1])))
users_contests_points = dict(sorted(users_contests_points.items(), key=lambda x: (x[0])))

print(f'Best candidate is {winer} with total {final_dic[winer]} points.')
print("Ranking:")
for k,t in users_contests_points.items():
   print(f"{k}")
   for m,v in users_contests_points[k].items():
        print(f"#  {m} -> {v}")
