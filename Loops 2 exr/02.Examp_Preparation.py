number_bad_score = int(input())

average_score = 0
count = 1
number_of_failers = 0
the_name = ''
is_he_fail = False

while the_name != "Enough":

    name_task = str(input())

    if name_task == "Enough":
        break

    the_name = name_task

    score = int(input())
    average_score += score

    count += 1

    if score <= 4:
        number_of_failers += 1
    if number_of_failers == number_bad_score:
        is_he_fail = True
        break

average_score /= (count -1)

if not is_he_fail:
    print(f"Average score:{average_score: .2f}")
    print(f"Number of problems: {count-1}")
    print(f"Last problem: {the_name}")

else:
    print(f'You need a break, {number_bad_score} poor grades.')
