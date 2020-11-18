budjet = float(input())
season = input()

location =""
price = 0
type = ""

if budjet <= 100:
    location = "Bulgaria"
    if season == "summer":
        price = budjet * 0.3
    elif season == "winter":
        price = budjet * 0.7
elif budjet <= 1000:
    location = "Balkans"
    if season == "summer":
        price = budjet * 0.4
    elif season == "winter":
        price = budjet * 0.8
elif budjet > 1000:
    location = "Europe"
    if season == "winter" or season == "summer":
        price = budjet * 0.9

if season == "summer" and location != "Europe":
    type = "Camp"
else:
    type = "Hotel"

print(f'Somewhere in {location}')
print(f'{type} -{price: .2f}')
