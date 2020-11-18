budjet = int(input())
season = input()
number_fishermen = int(input())

price_boat = 0
discount = 0
ad_discount = 0
price = 0

if season == "Spring":
    price_boat = 3000
elif season == "Summer":
    price_boat = 4200
elif season == "Autumn":
    price_boat = 4200
elif season == "Winter":
    price_boat = 2600

if number_fishermen <= 6:
    discount = price_boat * 0.1
elif 7 <= number_fishermen <= 11:
    discount = price_boat * 0.15
elif number_fishermen >= 12:
    discount = price_boat * 0.25

price = price_boat - discount

if number_fishermen % 2 == 0 and season != "Autumn":
    ad_discount = price * 0.05

total_price = price - ad_discount

if total_price > budjet:
    print(f'Not enough money! You need{total_price - budjet: .2f} leva.')
else:
    print(f'Yes! You have{budjet - total_price: .2f} leva left.')