name_student = str(input())

score = 0
count = 1

while count <= 12:
    score1 = float(input())
    count += 1
    if score1 < 4:
        count -= 1
    else:
        score += score1

average_score = score/12

print(f"{name_student} graduated. Average grade:{average_score: .2f}")


