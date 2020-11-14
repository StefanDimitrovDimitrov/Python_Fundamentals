rooms = int(input())

free_chairs = 0
needed_chairs = 0
room = 0
is_ok = True
for room in range(rooms):
    chairs = input().split()
    number_chairs = int(len(chairs[0]))
    people = int(chairs[1])
    room +=1
    if number_chairs < people:
        needed_chairs = people - number_chairs
        print(f'{needed_chairs} more chairs needed in room {room}')
        is_ok = False
    elif number_chairs >= people:
        free_chairs += number_chairs - people

if is_ok == True:
    print(f"Game On, {free_chairs} free chairs left")
