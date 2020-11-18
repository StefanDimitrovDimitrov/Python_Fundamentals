# num_floors = int(input())
# num_rooms = int(input())
#
# first_l = ''
# second_n = 0
# last_n = 0
#
# for i in range(1,num_floors):
#     if i % 2 == 0:
#         first_l = "0"
#         second_n = i
#     else:
#         first_l = "A"
#         second_n = i
#     for x in range(1,num_rooms):
#         last_n = x
#         print(f'{first_l}{second_n}{last_n}')
#
#
#

floors = int(input())
rooms = int(input())

for current_floor in range(floors, 0, -1):
    for current_room in range(0, rooms, 1):
        if current_floor == floors:
            print(f"L{current_floor}{current_room}", end= " ")
        elif current_floor % 2 == 0:
            print(f"O{current_floor}{current_room}", end= " ")
        elif current_floor % 2 == 1:
            print(f"A{current_floor}{current_room}", end = " ")
    print()