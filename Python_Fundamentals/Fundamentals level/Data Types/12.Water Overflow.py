n = int(input())

liter_tank = 0

for i in range(n):
    liter = int(input())
    liter_tank += liter
    if liter_tank > 255:
        print('Insufficient capacity!')
        liter_tank -= liter
        continue

print(liter_tank)
