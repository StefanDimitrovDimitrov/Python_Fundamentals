projection_type = input()
r = int(input())
c = int(input())

price = 0

if projection_type == "Premiere":
    price = r * c * 12
elif projection_type == "Normal":
    price = r * c * 7.5
else:
    price = r * c * 5

print(f'{price: .2f}')
