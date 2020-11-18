participants = int(input())

income = 0
total_number_cakes = 0

for each in range(participants):
    name = input()
    num_cookies = 0
    num_cakes = 0
    num_waffles = 0
    command = input()
    while command != "Stop baking!":
        cake_type = command
        number_cakes = int(input())
        total_number_cakes += number_cakes
        if cake_type == "cookies":
            num_cookies += number_cakes
            income += number_cakes * 1.5
        elif cake_type == "cakes":
            num_cakes += number_cakes
            income += number_cakes * 7.80
        elif cake_type == "waffles":
            num_waffles += number_cakes
            income += number_cakes * 2.3
        command = input()
    print(f"{name} baked {num_cookies} cookies, {num_cakes} cakes and {num_waffles} waffles.")
    num_cookies = 0
    num_cakes = 0
    num_waffles = 0

print(f"All bakery sold: {total_number_cakes}")
print(f"Total sum for charity:{income: .2f} lv.")
