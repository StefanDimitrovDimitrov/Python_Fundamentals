key = int(input())
n = int(input())

a = ""

for i in range(n):
    letter = input()
    a = ord(letter)
    a += key

    print(f'{chr(a)}', end="")

