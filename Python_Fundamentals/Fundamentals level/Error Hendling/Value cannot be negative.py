
class ValueCannotBeNegative(Exception):
    print("The value is lest than Zero")
    pass

input = int(input())

if input < 0:
    raise ValueCannotBeNegative