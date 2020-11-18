days_tournament = int(input())

money = 0
total_money = 0
count_win = 0
total_win = 0
count_lose = 0
total_lose = 0

the_tournament = True

while the_tournament:
    command = input()
    if command == "Finish":
        days_tournament -= 1

        if count_win > count_lose:
            money += money * 0.1

        total_money += money
        money = 0
        count_win = 0
        count_lose = 0

        if days_tournament == 0:
            the_tournament = False
            break
        continue
    result = input()

    if result == "win":
        money += 20
        count_win += 1
        total_win += 1
    else:
        count_lose += 1
        total_lose += 1


if total_win > total_lose:
    total_money += total_money * 0.2
    print(f"You won the tournament! Total raised money:{total_money: .2f}")
else:
    print(f"You lost the tournament! Total raised money:{total_money: .2f}")
