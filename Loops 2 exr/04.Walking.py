steps = 0
final_steps = 0
reach_the_goal = False
while steps < 10000:
    command = input()
    if command == "Going home":
        final_steps = int(input())
        steps += final_steps
        if steps < 10000:
            reach_the_goal = False
            break
        else:
            reach_the_goal = True
            break
    else:
        number = int(command)
        steps += number
        reach_the_goal = True

if reach_the_goal:
    print(f"Goal reached! Good job!")
else:
    print(f'{10000 - steps} more steps to reach goal.')


