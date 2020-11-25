import math
import exceptions


def find_circle_area(radius):
    if type(radius) not in [int, float]:
        raise exeptions.InvalidInputErrorutError(f"Radius cannot be of type {type(radius)}")

    return math.pi * (radius** 2)

try:
    print(find_circle_area(True))
except exceptions.InvalidInputError:
    print("Please enter valid input")
