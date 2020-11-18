days = int(input())
bakers = int(input())

cakes = int(input())
waffles = int(input())
pancakes = int(input())

price_of_cakes = cakes * 45
price_of_waffles = waffles * 5.8
price_of_pancakes = pancakes * 3.2

price_of_bakers = bakers * (price_of_cakes + price_of_waffles + price_of_pancakes)
total_price = days * price_of_bakers
expenses = total_price / 8

final_price = total_price - expenses

print(f"{final_price: .2f}")