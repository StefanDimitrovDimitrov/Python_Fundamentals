import math

sushi_type = input()
restaurant_name = input()
number_serving = int(input())
order = input()

price = 0
total_price = 0

is_real_restaurant_name = True

if restaurant_name == "Sushi Zone":
    if sushi_type == "sashimi":
        price = 4.99
    elif sushi_type == "maki":
        price = 5.29
    elif sushi_type == "uramaki":
        price = 5.99
    elif sushi_type == "temaki":
        price = 4.29
elif restaurant_name == "Sushi Time":
    if sushi_type == "sashimi":
        price = 5.49
    elif sushi_type == "maki":
        price = 4.69
    elif sushi_type == "uramaki":
        price = 4.49
    elif sushi_type == "temaki":
        price = 5.19
elif restaurant_name == "Sushi Bar":
    if sushi_type == "sashimi":
        price = 5.25
    elif sushi_type == "maki":
        price = 5.55
    elif sushi_type == "uramaki":
        price = 6.25
    elif sushi_type == "temaki":
        price = 4.75
elif restaurant_name == "Asian Pub":
    if sushi_type == "sashimi":
        price = 4.50
    elif sushi_type == "maki":
        price = 4.80
    elif sushi_type == "uramaki":
        price = 5.50
    elif sushi_type == "temaki":
        price = 5.50
else:
    is_real_restaurant_name = False

total_price = price * number_serving

if not is_real_restaurant_name:
    print(f'{restaurant_name} is invalid restaurant!')
elif order == "Y":
    total_price += total_price * 0.2
    print(f'Total price: {math.ceil(total_price)} lv.')
else:
    print(f'Total price: {math.ceil(total_price)} lv.')
