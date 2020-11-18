flower = input()
number_flowers = int(input())
budjet = int(input())

price = 0
discount = 0
ad_price = 0

if flower == "Roses":
    price = number_flowers * 5
    if number_flowers > 80:
        discount = price * 0.1
elif flower == "Dahlias":
    price = number_flowers * 3.8
    if number_flowers > 90:
        discount = price * 0.15
elif flower == "Tulips":
    price = number_flowers * 2.8
    if number_flowers > 80:
        discount = price * 0.15
elif flower == "Narcissus":
    price = number_flowers * 3
    if number_flowers < 120:
        ad_price = price *0.15
elif flower == "Gladiolus":
    price = number_flowers * 2.5
    if number_flowers < 80:
        ad_price = price * 0.2

if price * discount != 0:
    price = price - discount
else:
    price = price + ad_price

if price > budjet:
    print(f'Not enough money, you need{price - budjet: .2f} leva more.')
else:
    print(f'Hey, you have a great garden with {number_flowers} {flower} and{budjet-price: .2f} leva left.')
