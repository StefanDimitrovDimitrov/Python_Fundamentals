password = input()

while True:

    command = input()

    if command == "Done":
        break

    token = command.split(" ")[0]

    if token == "TakeOdd":
        list = []
        for i,t in enumerate(password):
            if i % 2 != 0:
                list.append(t)
        password = "".join(list)
        print(password)
    elif token == "Cut":
        start_index = int(command.split(" ")[1])
        length = int(command.split(" ")[2])
        end_index = start_index + length
        password = password[:start_index] + password[end_index:]
        print(password)
    elif token == "Substitute":
        substring = command.split(" ")[1]
        substitute = command.split(" ")[2]

        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")