money_for_vacation = float(input())
current_money = float(input())

count_days_spend = 0
count_of_spend = 0

if_she_save_money = True

while current_money < money_for_vacation and count_of_spend < 5:

    type_action = input()
    current_expence = float(input())

    count_days_spend += 1

    if type_action == "spend":
        current_money -= current_expence
        count_of_spend += 1
        if current_expence > current_money:
            current_money = 0
    else:
        current_money += current_expence
        count_of_spend = 0

    if count_of_spend == 5:
        if_she_save_money = False
        break

if if_she_save_money:
    print(f"You saved the money for {count_days_spend} days.")
else:
    print(f"You can't save the money.")
    print(f"{count_days_spend}")
