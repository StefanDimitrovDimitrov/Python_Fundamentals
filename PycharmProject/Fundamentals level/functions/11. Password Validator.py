def length(password):
    return True if 6 <= len(password) <= 10 else False


def letter_digits(password):
    validation = 0
    for i in password:
        if ord("a") <= ord(i) <= ord("z") or ord("A") <= ord(i) <= ord("Z") or ord("0") <= ord(i) <= ord("9"):
            validation += 1
    return True if validation == len(password) else False

def two_digits(password):
    dig = 0
    for i in password:
        if chr(48) < i < chr(57):
            dig += 1

    return True if dig >= 2 else False


password = str(input())

if letter_digits(password) and length(password) and two_digits(password):
    print("Password is valid")

if not letter_digits(password):
    print("Password must consist only of letters and digits")

if not length(password):
    print("Password must be between 6 and 10 characters")

if not two_digits(password):
    print("Password must have at least 2 digits")
