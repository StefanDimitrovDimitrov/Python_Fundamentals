n = int(input())

min_number = +9999999

for i in range(n):
    number = int(input())
    while number < min_number:
        min_number = number
print(min_number)