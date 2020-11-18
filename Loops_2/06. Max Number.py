n = int(input())

max_number = -9999999

for i in range(n):
    number = int(input())
    while number > max_number:
        max_number = number
print(max_number)


