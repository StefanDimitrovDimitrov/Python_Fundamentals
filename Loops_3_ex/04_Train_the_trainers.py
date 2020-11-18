judges = int(input())

presentation_name = ""
presentation_score = 0
total_score = 0
count = 0
aver_score = 0
number_score = 0

while True:
    presentation_name = str(input())
    if presentation_name == "Finish":
        break
    else:
        for i in range(judges):
            score = float(input())
            total_score += score
            presentation_score += score
            number_score += 1
            count += 1
            if count == judges:
                aver_score = presentation_score/judges
                presentation_score = 0
                count = 0
                print(f"{presentation_name} -{aver_score: .2f}.")
print(f"Student's final assessment is{total_score/number_score: .2f}.")
