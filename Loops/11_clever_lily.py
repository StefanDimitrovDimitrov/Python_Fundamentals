lili_age = int(input())
price_washing_machine = float(input())
a_toy_price = int(input())

money = 0
present = 0
num_toy = 0

for i in range(1, lili_age + 1):
    if i % 2 == 0:
        money += 10
        present = present + money - 1
    else:
        num_toy += 1

income_toys = num_toy * a_toy_price

total_money = present + income_toys

if total_money >= price_washing_machine:
    print(f'Yes!{total_money - price_washing_machine: .2f}')
else:
    print(f'No!{price_washing_machine - total_money: .2f}')
