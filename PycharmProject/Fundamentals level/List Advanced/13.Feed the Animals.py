animals = []
areas = []


class Animal:
    def __init__(self, animal_name, daily_food_limit, area):
        self.animal_name = animal_name
        self.daily_food_limit = daily_food_limit
        self.area = area

    def return_final_state(self):
        return f'{self.animal_name} -> {self.daily_food_limit}g'


class AnimalArea:
    def __init__(self, name, count):
        self.name = name
        self.number_animals = count

    def hungry_animals(self):
        return f'{self.name} : {self.number_animals}'


while True:
    command = input()
    if command == "Last Info":
        break

    commands = command.split(":")

    instruction = commands[0]
    animal_name = commands[1]
    food = commands[2]
    area = commands[3]

    tool = False
    if instruction == "Add":
        tool = False
        for x in animals:
            if x.animal_name == animal_name:
                new_food = int(x.daily_food_limit) + int(food)
                x.daily_food_limit = new_food
                tool = True

        if not tool:
            current_animal = Animal(animal_name,food,area)
            animals.append(current_animal)


    elif instruction == "Feed":
        for x in animals:
            if str(x.animal_name) == animal_name:
                new_food = int(x.daily_food_limit) - int(food)
                x.daily_food_limit = new_food
            if int(x.daily_food_limit) <= 0:
                print(f'{animal_name} was successfully fed')
                animals.remove(x)

print("Animals:")
sorted_animals = sorted(animals, key=lambda x: x.animal_name, reverse=False)
sorted_animals = sorted(sorted_animals, key=lambda x: int(x.daily_food_limit), reverse=True)

for x in sorted_animals:
    print(x.return_final_state())

the_place_exist = False
for z in animals:
    the_place_exist = False
    for x in areas:
        if x.name == z.area:
            x.number_animals += 1
            the_place_exist = True

    if not the_place_exist:
        current_place = AnimalArea(z.area, 1)
        areas.append(current_place)

sorted_areas = sorted(areas, key=lambda x: int(x.number_animals), reverse=True)

print('Areas with hungry animals:')
for c in sorted_areas:
    print(c.hungry_animals())
