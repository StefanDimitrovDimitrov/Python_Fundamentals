string = str(input())

while True:

    action = input()

    if action == "Travel":
        break

    command = action.split(":")[0]

    if command == "Add Stop":
        index = int(action.split(":")[1])
        text = action.split(":")[2]
        if len(string) > index:
            string = string[:index] + text + string[index::]
        print(string)
    if command == "Remove Stop":
        start_index = int(action.split(":")[1])
        end_index = int(action.split(":")[2])

        if start_index >= 0 and start_index < len(string) and end_index >= 0 and end_index < len(string):
            string = string[0:start_index:] + string[end_index+1::]
        print(string)
    if command == "Switch":
        old_string = action.split(":")[1]
        new_string = action.split(":")[2]

        if old_string in string:
            string = string.replace(old_string,new_string)
        print(string)

print(f"Ready for world tour! Planned stops: {string}")