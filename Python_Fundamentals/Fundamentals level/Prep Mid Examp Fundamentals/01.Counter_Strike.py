initial_energy = int(input())

win_count = 0
result_1 = ""
result_2 = ""

while True:
    command = input()

    if command == "End of battle":
        print(f"Won battles: {win_count}. Energy left: {initial_energy}")
        break

    distance = int(command)


    if initial_energy >= distance:
        initial_energy -= distance
        win_count += 1

        if win_count % 3 == 0:
            initial_energy += win_count
    else:
        print(f"Not enough energy! Game ends with {win_count} won battles and {initial_energy} energy")
        break


