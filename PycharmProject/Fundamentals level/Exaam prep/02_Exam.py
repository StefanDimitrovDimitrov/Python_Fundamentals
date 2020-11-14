import math

width = float(input())
length = float(input())
height = float(input())
avr_height_astronauts = float(input())

volume_racket = width * length * height
volume_room = (avr_height_astronauts + 0.40)*2 * 2

num_astronauts = volume_racket // volume_room

if num_astronauts < 3:
    print(f"The spacecraft is too small.")
elif num_astronauts > 10:
    print("The spacecraft is too big.")
else:
    print(f"The spacecraft holds {math.floor(num_astronauts)} astronauts.")

