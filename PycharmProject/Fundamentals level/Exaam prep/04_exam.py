num_passengers = int(input())
num_stops = int(input())


for stops in range(num_stops):
    num_down = int(input())
    num_up = int(input())

    if stops % 2 == 0:
        num_up += 2
    else:
        num_down += 2

    num_passengers = num_passengers - num_down + num_up

print(f"The final number of passengers is : {num_passengers}")
