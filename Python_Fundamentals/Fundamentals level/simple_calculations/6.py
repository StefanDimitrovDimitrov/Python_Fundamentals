# 1. Read input data
dogs_count = input()
other_animals_count = input()
# 2. Convert date to the correct type
dogs_count = int(dogs_count)
other_animals_count= int(other_animals_count)
# 3. Calculate money needed for dog food
dog_food_cost = dogs_count *2.5
# 4. Calculate money needed for other animals food
other_animals_food_cost = other_animals_count * 4

# 5. Calculate total

total_cost = dog_food_cost + other_animals_food_cost
# 6. Print and format
print(f'{total_cost:.2f} lv.')
