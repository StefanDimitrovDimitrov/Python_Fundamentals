sides = {}

while True:
    line = input()

    if line == "Lumpawaroo":
        break

    if " | " in line:
        side = line.split(" | ")[0]
        user = line.split(" | ")[1]

        if side not in sides:
            sides[side] = []

        asd = sides.values()
        all_values = []

        for current_list in sides.values():
            all_values += current_list

        if user not in all_values:
            sides[side].append(user)
    else:
        user = line.split(" -> ")[0]
        side = line.split(" -> ")[1]
        old_side = ""

        for k, v in sides.items():
            if user in v:
                old_side = k
                break

        if old_side != "":
            sides[old_side].remove(user)

            if side not in sides:
                sides[side] = []

            sides[side].append(user)
        else:
            if side not in sides:
                sides[side] = []
            sides[side].append(user)

        print(f"{user} joins the {side} side!" )

sides = dict(sorted(sides.items(), key=lambda x: (-len(x[1]), x[0])))

for side, users in sides.items():
    if len(users) == 0:
        continue
    print(f"Side: {side}, Members: {len(users)}")

    for user in sorted(users):
        print(f"! {user}")
