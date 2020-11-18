sum = int(float(input()) * 100)


count = 0


while sum != 0:
    if sum >= 200:
        sum -= 200
    elif 100 <= sum < 200:
        sum -= 100
    elif 50 <= sum < 100:
        sum -= 50
    elif 20 <= sum < 50:
        sum -= 20
    elif 10 <= sum < 20:
        sum -= 10
    elif 5 <= sum < 10:
        sum -= 5
    elif 2 <= sum < 5:
        sum -= 2
    elif 1 <= sum <= 2:
        sum = 0
    count += 1

print(f'{count}')
