cruise = str(input())
cabin = str(input())
nights = int(input())

price = 0

if cruise == "Mediterranean":
    if cabin == "standard cabin":
        price = 27.50
    elif cabin == "cabin with balcony":
        price = 30.20
    elif cabin == "apartment":
        price = 40.50
elif cruise == "Adriatic":
    if cabin == "standard cabin":
        price = 22.99
    elif cabin == "cabin with balcony":
        price = 25.00
    elif cabin == "apartment":
        price = 34.99
elif cruise == "Aegean":
    if cabin == "standard cabin":
        price = 23.00
    elif cabin == "cabin with balcony":
        price = 26.60
    elif cabin == "apartment":
        price = 39.80

sum = 4 * price * nights

if nights > 7:
    sum -= sum * 0.25

print(f" Annie's holiday in the {cruise} sea costs{sum: .2f} lv.")
