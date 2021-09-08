quantity = int(input())
days = int(input())

christmas_spirit = 0
days_to_christmas = 0
total_spirit = 0
budget = 0

if days % 10 == 0:
    christmas_spirit -= 30

while days != days_to_christmas:
    days_to_christmas += 1

    if days_to_christmas % 11 ==0:
        quantity += 2

    if days_to_christmas % 2 == 0:
        christmas_spirit += 5
        budget += 2*quantity
    if days_to_christmas % 3 == 0:
        christmas_spirit += 13
        budget += 5 * quantity + 3 * quantity
    if days_to_christmas % 5 == 0:
        christmas_spirit += 17
        budget += 15*quantity
        if days_to_christmas % 3 == 0:
            christmas_spirit += 30
    if days_to_christmas % 10 == 0:
        christmas_spirit -= 20
        budget += 5 + 3 + 15


print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_spirit}")
