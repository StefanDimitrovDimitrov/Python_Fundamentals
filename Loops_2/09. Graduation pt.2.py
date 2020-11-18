name_student = str(input())

score = 0
count = 1
number_of_failer = 0
average_score = 0
is_expelled = False

while count <= 12:
    score1 = float(input())
    if score1 >= 4:
        count+=1
        score += score1
    else:
        number_of_failer += 1
        if number_of_failer == 2:
            is_expelled = True
            print(f'{name_student} has been excluded at {count} grade')
            break

if not is_expelled:
    average_score = score / 12
    print(f"{name_student} graduated. Average grade:{average_score: .2f}")
