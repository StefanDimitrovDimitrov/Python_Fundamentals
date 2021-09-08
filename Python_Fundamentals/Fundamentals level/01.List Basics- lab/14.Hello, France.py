items = input().split("|")
budget = int(input())

price_item1 = 0
price_item2 = 0
price_item3 = 0
cost = 0


for item in items:
    args = item.split("->")
    item_name = args[0]
    price_name = float(args[1])

    if budget >= price_name:

        if item_name == "Clothes" and price_name <= 50:
            budget -= price_name
            cost += price_name
            price_name *= 1.4
            price_item1 += price_name
            print(f'{price_name:.2f}', end =" ")
        elif item_name == "Shoes" and price_name <= 35:
            budget -= price_name
            cost += price_name
            price_name *= 1.4
            price_item2 += price_name
            print(f'{price_name:.2f}', end =" ")
        elif item_name == "Accessories" and price_name <= 20.50:
            budget -= price_name
            cost += price_name
            price_name *= 1.4
            price_item3 += price_name
            print(f'{price_name:.2f}', end =" ")

profit = price_item1 + price_item2 + price_item3 - cost
new_budget = price_item1 + price_item2 + price_item3 + budget

print(f'\nProfit: {profit:.2f}')

if new_budget >= 150:
    print('Hello, France!')
else:
    print("Time to go.")