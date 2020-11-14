guest_singer_price = int(input())

command = ""
cover = 0
total_guest = 0
is_restauran_is_full = False


while not is_restauran_is_full:
    command = input()
    if command == "The restaurant is full":
        is_restaurant_is_fill = True
        break
    else:
        num_guest = int(command)

    total_guest += num_guest

    if num_guest < 5:
         cover += num_guest * 100
    else:
        cover += num_guest * 70

if cover >= guest_singer_price:
    print(f"You have {total_guest} guests and {cover - guest_singer_price} leva left.")
else:
    print(f"You have {total_guest} guests and {cover} leva income, but no singer.")



