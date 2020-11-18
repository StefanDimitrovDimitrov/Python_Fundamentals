def swap(command):

    index_1 = int(command[1])
    index_2 = int(command[2])

    list[index_1], list[index_2] = list[index_2], list[index_1]
    return list


def multiply(command):

    index_1 = int(command[1])
    index_2 = int(command[2])

    result = list[index_1] * list[index_2]

    list[index_1] = result

    return list

def decrease(list):
    list = [x - 1 for x in list]

    return list

list_01 = input().split()
list = list(map(int, list(list_01)))

while True:
    command = input()

    if command == "end":
        break

    command = command.split()

    if command[0] == "swap":
        swap(command)
    elif command[0] == "multiply":
        multiply(command)
    elif command[0] == "decrease":
        list = decrease(list)


list = [str(x) for x in list]

list = ", ".join(list)

print(list)