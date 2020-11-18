import math

player_name = input()
number_games = int(input())

total = 0
current_score_vol = 0
current_score_ten = 0
current_score_bad = 0

avr_score_vol = 0
avr_score_ten = 0
avr_score_bad = 0

count_vol = 0
count_ten = 0
count_bad = 0

for game in range(number_games):
    name_game = input()
    score = int(input())

    if name_game == "volleyball":
        count_vol += 1
        score = score * 1.07
        current_score_vol += score

    elif name_game == "tennis":
        count_ten += 1
        score = score * 1.05
        current_score_ten += score

    elif name_game == "badminton":
        count_bad += 1
        score = score * 1.02
        current_score_bad += score

total = current_score_vol + current_score_ten + current_score_bad
avr_score_vol = math.floor(current_score_vol / count_vol)
avr_score_ten = math.floor(current_score_ten / count_ten)
avr_score_bad = math.floor(current_score_bad / count_bad)

if avr_score_bad >= 75 and avr_score_ten >= 75 and avr_score_vol >= 75:

    print(f"Congratulations, {player_name}! You won the cruise games with {math.floor(total)} points.")
else:
    print(f'Sorry, {player_name}, you lost. Your points are only {math.floor(total)}.')
