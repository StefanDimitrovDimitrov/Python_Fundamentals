username = input()

while True:

    instructions = input()

    if instructions == "Sign up":
        break

    instructions = instructions.split()
    command = instructions[0]

    if command == "Case":
        if instructions[1] == "lower":
            username = username.lower()
        elif instructions[1] == "upper":
            username = username.upper()
        print(username)
    elif command == "Reverse":
        start_index = int(instructions[1])
        end_index = int(instructions[2])+1

        # if start_index >= 0 or start_index < len(username) or end_index >= 0 or end_index < len(username):
        #     result = username[start_index:end_index+1]
        #     result = result[::-1]
        #     print(result)
        if end_index <= len(username):
            result = username[start_index:end_index]
            result = result[::-1]
            print(result)

    elif command == "Cut":
        substring = instructions[1]

        if substring in username:
            username = username.replace(substring,"")
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")
    elif command == "Replace":
        char = instructions[1]
        username = username.replace(char, "*")
        print(username)
    elif command == "Check":
        chart = instructions[1]

        if chart in username:
            print("Valid")
        else:
            print(f"Your username must contain {chart}.")

