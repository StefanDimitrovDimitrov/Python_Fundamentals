width = int(input())
lengh = int(input())
hieght = int(input())

room_capacity = width * lengh * hieght
free_space = room_capacity
is_done_moving = False
while free_space > 0:
    command = input()
    if command == "Done":
        is_done_moving = True
        break
    num_box = int(command)
    free_space -= num_box


if is_done_moving:
    print(f'{free_space} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(free_space)} Cubic meters more.')






