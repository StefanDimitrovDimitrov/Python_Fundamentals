cards = input().split()

team_a = [1] * 11
team_b = [1] * 11

for card in cards:
    tokens = card.split("-")
    team = tokens[0]
    player = int(tokens[1])

    if team =="A":
        team_a[player - 1] = 0
    else:
        team_b[player -1] = 0