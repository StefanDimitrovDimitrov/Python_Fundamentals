number = int(input())

count = 0
result = []

while True:
    count += 1
    capacity_shell = 2*count**2

    number -= capacity_shell
    if number <= 0:
        result.append(capacity_shell + number)
        break
    else:
        result.append(capacity_shell)

print(result)