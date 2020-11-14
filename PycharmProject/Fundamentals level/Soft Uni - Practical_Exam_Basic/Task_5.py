capacity = float(input())

current_space = capacity
space = 0
count = 0
suitcase_num = 0

while space <= capacity:
    command = input()
    if command == "End":
        print(f"Congratulations! All suitcases are loaded!")
        break
    else:
        suitcase = float(command)

        count += 1
        if count % 3 == 0:
            suitcase += suitcase * 0.1

        if suitcase >= current_space:
            print("No more space!")
            break
        suitcase_num +=1
        current_space -= suitcase
        space += suitcase
print(f"Statistic: {suitcase_num} suitcases loaded.")
