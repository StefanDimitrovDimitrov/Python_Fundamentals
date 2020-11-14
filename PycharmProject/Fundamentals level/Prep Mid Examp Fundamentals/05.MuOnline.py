def potion(command,initial_health):
    a = command.split()
    current_initial_health = initial_health + int(a[1])
    if current_initial_health > 100:
        healt = abs(current_initial_health - (100 + int(a[1])))

        print(f"You healed for {healt} hp.")
    else:
        print(f"You healed for {a[1]} hp.")

    if current_initial_health <= 100:
        print(f"Current health: {current_initial_health} hp.")
    else:
        print(f"Current health: {100} hp.")
        current_initial_health = 100

    return current_initial_health


def chest(command,initial_bitcoions):
    b = command.split()
    t = initial_bitcoions + int(b[1])
    print(f"You found {b[1]} bitcoins.")
    return t



def boss(command,initial_health):

    c = command.split()
    current_initial_health = initial_health - int(c[1])

    if current_initial_health > 0:
        print(f"You slayed {c[0]}.")
    else:
        print(f"You died! Killed by {c[0]}.")

    return current_initial_health

command = input().split("|")



initial_health = 100
initial_bitcoins = 0

current_bitcoins = 0

for i,item in enumerate(command):
    if (command[i]).__contains__("potion"):
        instruction = command[i]
        initial_health = potion(instruction,initial_health)

    elif(command[i]).__contains__("chest"):
        current_bitcoins += chest(command[i],initial_bitcoins)
    else:
        initial_health = boss(command[i],initial_health)
        if initial_health <= 0:
            print(f"Best room: {i+1}")
            break

if initial_health > 0:
    print("You've made it!")
    print(f"Bitcoins: {current_bitcoins}")
    print(f"Health: {initial_health}")