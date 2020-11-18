incomes = int(input())

new_income = 0
total = 0
for i in range(incomes):
    new_income = float(input())
    if new_income >= 0:
        total = total + new_income
        print(f"Increase: {new_income:.2f}")
    else:
        print(f"Invalid operation!")
        break

print(f"Total: {total:.2f}")

