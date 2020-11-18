import math

Time_first = int(input())
Time_second = int(input())
Time_third = int(input())

total_time = Time_first + Time_second + Time_third

minutes = total_time / 60
seconds = total_time % 60

minutes = math.floor(minutes)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')