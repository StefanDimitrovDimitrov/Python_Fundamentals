import math

year = (input())
number_of_holidays = int(input())
number_of_weekends = int(input())

weekends_Sofia = 48 - number_of_weekends
games_in_Sofia = weekends_Sofia * 3 / 4
games_during_holidays = number_of_holidays * 2 / 3

total_games = games_in_Sofia + number_of_weekends + games_during_holidays

if year == "leap":
    total_games += total_games * 0.15
else:
    total_games

print(math.floor(total_games))
