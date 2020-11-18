import math

record_sec = float(input())
distance_met = float(input())
time_sec = float(input())

goal = distance_met * time_sec
add = math.floor(distance_met / 50)
add_total = add * 30
total_time = goal + add_total

if total_time >= record_sec:
    print(f"No! He was{total_time - record_sec: .2f} seconds slower.")
else:
    print(f" Yes! The new record is{total_time: .2f} seconds.")
