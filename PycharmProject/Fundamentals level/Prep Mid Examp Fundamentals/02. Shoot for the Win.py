the_target = input().split()

targets = list(map(int, the_target))

current_num = 0
shots = 0
while True:

    command = input()

    if command == "End":
        break

    command = int(command)

    if command < len(targets):
        if targets[command] == -1:
            continue

        current_num = targets[command]

        targets[command] = -1
        shots += 1

        for i, item in enumerate(targets):
            if item > current_num and item > -1:
                targets[i] -= current_num
            elif item <= current_num and item > -1:
                targets[i] += current_num
    else:
        continue

result =",".join([str(n) for n in targets])

print(f'Shot targets: {shots} -> {result}')
# print(f'Shot targets: {shots} -> ', end="")
# for r in targets:
#     print(f'{r}, ', end="")
