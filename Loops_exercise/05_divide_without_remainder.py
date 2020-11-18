n = int(input())

p1 = 0
p2 = 0
p3 = 0

x1 = 0
x2 = 0
x3 = 0

for i in range(n):
    number = int(input())

    if number % 2 == 0:
        x1 += 1
        p1 = (x1 / n) * 100
    if number % 3 == 0:
        x2 += 1
        p2 = (x2 / n) * 100
    if number % 4 == 0:
        x3 += 1
        p3 = (x3 / n) * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')