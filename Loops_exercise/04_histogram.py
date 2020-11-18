n = int(input())

x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(n):
    number = int(input())

    if number < 200:
        x1 += 1
        p1 = (x1 / n) * 100
    elif 200 <= number < 400:
        x2 += 1
        p2 = (x2 / n) * 100
    elif 400 <= number < 600:
        x3 += 1
        p3 = (x3 / n) * 100
    elif 600 <= number < 800:
        x4 += 1
        p4 = (x4 / n) * 100
    elif 800 <= number:
        x5 += 1
        p5 = (x5 / n) * 100

print(f'{p1: .2f}%')
print(f'{p2: .2f}%')
print(f'{p3: .2f}%')
print(f'{p4: .2f}%')
print(f'{p5: .2f}%')
