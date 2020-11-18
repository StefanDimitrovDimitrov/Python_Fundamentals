points = int(input())

count = 0
the_game_is_finished = False

while points > 0:
    sector = input()
    count += 1

    if sector == "bullseye":
        the_game_is_finished = True
        break

    current_points = int(input())

    if sector == "double ring":
        current_points *= 2
    elif sector == "triple ring":
        current_points *= 3
    points -= current_points

if the_game_is_finished:
    print(f"Congratulations! You won the game with a bullseye in {count} moves!")
elif points == 0:
    print(f"Congratulations! You won the game in {count} moves!")
else:
    print(f" Sorry, you lost. Score difference: {abs(points)}.")


