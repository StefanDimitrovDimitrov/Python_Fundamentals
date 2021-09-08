def loading_bar(number):

    a = int(number[0]) * "%"
    b = (10 - int(number[0])) * "."

    if int(number) == 100:
        a = 10 * "%"
        b = 0 *"."

    c = a+b
    return f'{c}'

number = str(input())

if number == "100":
    print(f'{number}% Complete!')
    print(f"[{loading_bar(number)}]")
else:
    print(f'{number}% [{loading_bar(number)}]')
    print(f'Still loading...')
