def shoot(second_command, targets):
    index = int(second_command.split(" ")[1])
    power = int(second_command.split(" ")[2])

    if (index < len(targets)) and index >= 0:
        targets[index] -= power

        if targets[index] <= 0:
            del targets[index]


def add(second_command, targets):
    index = int(second_command.split(" ")[1])
    value = int(second_command.split(" ")[2])

    if (index < len(targets)) and index >= 0:
        targets.insert(index, value)
    else:
        print("Invalid placement!")


def strike(second_command, targets):
    index = int(second_command.split(" ")[1])
    radius = int(second_command.split(" ")[2])

    if (radius + index < len(targets)) and (index - radius) >= 0:
        del targets[(index - radius):(radius + index+1)]
    else:
        print("Strike missed!")


target = input().split()
targets = list(map(int, target))

while True:

    second_command = input()

    if second_command == "End":
        break

    action = second_command.split(" ")[0]
    if action == "Shoot":
        shoot(second_command, targets)
    elif action == "Add":
        add(second_command, targets)
    elif action == "Strike":
        strike(second_command, targets)

print("|".join((map(str, targets))))
