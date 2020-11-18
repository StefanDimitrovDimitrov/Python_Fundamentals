def urgent(list,command):
    if not command[1] in list:
        list.insert(0,command[1])
    return list


def unnecessary(list, command):
    if command[1] in list:
        list.remove(command[1])


def correct(list,command):
    for i in range(len(list)):
        if list[i] == command[1]:
            list[i] = command[2]


def rearrange(list,command):
    if command[1] in list:
        list.remove(command[1])
        list.append(command[1])

list = input()

list = list.split("!")

while True:
    command = input()

    if command == "Go Shopping!":
        break

    command = command.split()

    if command[0] == "Urgent":
        urgent(list,command)
    if command[0] == "Unnecessary":
        unnecessary(list,command)
    if command[0] == "Correct":
        correct(list,command)
    if command[0] == "Rearrange":
        rearrange(list, command)

print(", ".join(list))
