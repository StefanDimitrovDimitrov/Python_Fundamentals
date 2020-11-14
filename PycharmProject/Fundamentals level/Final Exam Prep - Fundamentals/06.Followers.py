
record = {}
followers = set()
res_dic = {}

while True:
    commands = input()
    if commands == "Log out":
        break

    command = commands.split(": ")[0]
    username = commands.split(": ")[1]

    followers.add(username)

    if username not in record.keys() and command != "Blocked":
        record[username] = {}
        record[username]["likes"] = 0
        record[username]["comments"] = 0


    if command == "Like":
        count = commands.split(": ")[2]
        record[username]["likes"] += int(count)
    elif command == "Comment":
        record[username]["comments"] += 1
    elif command == "Blocked":
        if username in record.keys():
            del record[username]
            followers.remove(username)
        else:
            print(f"{username} doesn't exist.")


for username in followers:
    res_dic[username] = record[username]["likes"] + record[username]["comments"]

res_dic = dict(sorted(res_dic.items(), key= lambda x: (-x[1], x[0])))

# user_stats = dict(sorted(user_stats.items(), key= lambda x: (-x[1], x[0])))

print(f"{len(followers)} followers")

for k,v in res_dic.items():
    print(f"{k}: {v}")

