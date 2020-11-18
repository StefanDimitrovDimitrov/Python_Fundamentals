is_finish = False

while not is_finish:
    command = str(input())
    if command == "End":
        break
    need_money = float(input())
    while need_money > 0:
        incomes = float(input())
        need_money -= incomes
    print(f'Going to {command}!')