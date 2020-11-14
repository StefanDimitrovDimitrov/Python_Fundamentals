list_houses = input()
if len(list_houses)>1:
    list_houses = list_houses.split("@")
    list_houses = list(map(int,list_houses))
else:
    list_houses = list(map(int, list_houses[0]))

house_index = 0
last_position = 0
house_count = 0
triger = 0

while True:
    command = input()

    if command == "Love!":
        break
    command = command.split()

    num_house = int(command[1])
    # num_house = list(map(list,command))

    last_position += num_house

    if num_house < (len(list_houses[house_index:])):

        house_index = last_position

        if list_houses[last_position] == 0:
            print(f"Place {last_position} already had Valentine's day.")

        list_houses[last_position] -= 2

        if list_houses[last_position] == 0:
            print(f"Place {last_position} has Valentine's day.")
            house_count += 1
    else:

        if list_houses[0] == 0:
            print(f"Place {0} already had Valentine's day.")
        else:
            list_houses[0] -= 2

            if list_houses[0] == 0:
                print(f"Place {0} has Valentine's day.")
                house_count += 1

        last_position = 0
        house_index = 0


print(f"Cupid's last position was {last_position}.")

if house_count == len(list_houses):

    print(f"Mission was successful.")

else:
    print(f"Cupid has failed {len(list_houses) - house_count} places.")