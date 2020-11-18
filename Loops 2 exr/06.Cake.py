h_cake = int(input())
l_cake = int(input())

cake = h_cake * l_cake
total_piece = 0
is_cake_finished = False

while total_piece < cake:
    command = input()
    if command == "STOP":
        is_cake_finished = True
        break
    else:
        total_piece += int(command)


if not is_cake_finished:
    print(f'No more cake left! You need { total_piece - cake} pieces more.')
else:
    print(f'{cake - total_piece} pieces are left.')