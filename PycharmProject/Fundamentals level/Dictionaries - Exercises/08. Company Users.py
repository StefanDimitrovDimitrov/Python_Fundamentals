company_users = {}

while True:
    command = input()

    if command == "End":
        break

    company_name = command.split(" ->")[0]
    id = command.split(" ->")[1]


    if company_name not in company_users:
        company_users[company_name] = []
        company_users[company_name].append(id)
    else:
        if id not in [x for v in company_users.values() for x in v]:
            company_users[company_name].append(id)

company_users = dict(sorted(company_users.items(), key = lambda x: x[0]))

for k,v in company_users.items():
    print(f"{k}")
    for x in v:
        print(f"--{''.join(x)}")


