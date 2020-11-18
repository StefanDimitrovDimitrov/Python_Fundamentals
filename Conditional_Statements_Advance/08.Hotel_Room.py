month = input()
count_night = int(input())

price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
    if count_night > 14:
        price_studio *= 0.7
    elif count_night > 7:
        price_studio *= 0.95
elif month == "June" or month == "September":
    price_studio = 75.2
    price_apartment = 68.7
    if count_night > 14:
        price_studio *= 0.8
else:
    price_studio = 76
    price_apartment = 77

if count_night > 14:
    price_apartment *= 0.9

print(f'Apartment:{price_apartment * count_night: .2f} lv.')
print(f'Studio:{price_studio * count_night: .2f} lv.')
