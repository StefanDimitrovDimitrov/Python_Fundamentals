number = int(input())

for x in range(number):
    for z in range(number):
        for y in range(number):
            char_one = chr(97+x)
            char_two = chr(97+z)
            char_three = chr(97+y)
            print(f'{char_one}{char_two}{char_three}')