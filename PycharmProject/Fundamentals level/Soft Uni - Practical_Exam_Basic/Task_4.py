days = int(input())
food = float(input())

dog_food_day = 0
cat_food_day = 0
count_days = 0
biscuits = 0


for day in range(days):
    dog_food = int(input())
    cat_food = int(input())

    dog_food_day += dog_food
    cat_food_day += cat_food
    count_days += 1

    if count_days % 3 == 0:
        biscuits += (dog_food + cat_food) * 0.1

total_eaten_food = (dog_food_day + cat_food_day)
total_eaten_food_per = total_eaten_food / food * 100

total_food_dog = dog_food_day / total_eaten_food * 100
total_food_cat = cat_food_day / total_eaten_food * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_eaten_food_per:.2f}% of the food has been eaten.")
print(f"{total_food_dog:.2f}% eaten from the dog.")
print(f"{total_food_cat:.2f}% eaten from the cat.")



