from _collections import defaultdict

contest_dic = defaultdict(int)
user_stats = defaultdict(int)
list_users = set()

p  = 1
while True:
    command = input()

    if command == "no more time":
        break

    username,contest_name,points = command.split(" -> ")

    points = int(points)

    list_users.add(username)

    if contest_name not in contest_dic.keys():
        contest_dic[contest_name] = {username:points}
    else:
        if username in contest_dic[contest_name].keys():
            for k,v in contest_dic[contest_name].items():

                if k == username:
                    if v < points:
                        contest_dic[contest_name].update({username:points})
        else: contest_dic[contest_name].update({username:points})
for k in contest_dic.keys():
    for k,v in contest_dic[k].items():
        for n in list_users:
            if n == k:
                user_stats[k] += v

for k in contest_dic.keys():
    for t,v in contest_dic[k].items():
        contest_dic[k] = dict(sorted(contest_dic[k].items(), key= lambda x: (-x[1], x[0])))


user_stats = dict(sorted(user_stats.items(), key= lambda x: (-x[1], x[0])))

for k in contest_dic.keys():
    p = 1
    print(f"{k}: {len(contest_dic[k])} participants")
    for t,v in contest_dic[k].items():
        print(f"{p}. {t} <::> {v}")
        p+=1
print("Individual standings:")
p = 1
for s,m in user_stats.items():

    print(f"{p}. {s} -> {m}")
    p+=1