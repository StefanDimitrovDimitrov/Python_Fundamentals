first_number = int(input())
second_number = int(input())
third_number = int(input())

n_combination = 0
is_the_right_combination = False

for x in range(first_number, second_number + 1):
    for y in range(first_number, second_number + 1):
        n_combination += 1
        if x + y == third_number:
            is_the_right_combination = True
            break
    if is_the_right_combination:
        break

if is_the_right_combination:
    print(f"Combination N:{n_combination} ({x} + {y} = {third_number})")
else:
    print(f"{n_combination} combinations - neither equals {third_number}")
