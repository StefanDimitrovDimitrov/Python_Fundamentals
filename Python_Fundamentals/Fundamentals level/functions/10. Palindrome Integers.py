def is_palindrom(number):
    reversed_num = number[::-1]

    return True if reversed_num == number else False


text = input().split(', ')

for t in text:
    print(is_palindrom(t))