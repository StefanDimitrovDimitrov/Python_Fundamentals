n = int(input())
sum = 0

for x in range(n):
    letter = input()
    sum += ord(letter)
print(f"The sum equals: {sum}")
