def out_of_stock(name_gifts, items):
    for i, item in enumerate(name_gifts):
        if item == items[0]:
            name_gifts[i] = "None"

    # return name_gifts


def required(name_gifts, items):
    if int(items[1]) < len(name_gifts) and int(items[1]) > 0:
        name_gifts[int(items[1])] = items[0]


def just_in_case(name_gifts, items):
    name_gifts[-1] = items[0]


name_gifts = input().split()

have_money = True

while True:
    command = input()

    if command == "No Money":
        have_money = False
        break

    items = command.split()[1:]
    command = command.split()

    if command[0] == "OutOfStock":
        out_of_stock(name_gifts, items)
    if command[0] == "Required":
        required(name_gifts, items)
    if command[0] == "JustInCase":
        just_in_case(name_gifts, items)

if "None" in name_gifts:
    name_gifts = list(filter(lambda a:a != "None",name_gifts))

print(" ".join(name_gifts))
