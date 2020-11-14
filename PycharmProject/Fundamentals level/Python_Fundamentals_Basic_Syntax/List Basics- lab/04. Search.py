n = int(input())

word = input()

string = [input() for _ in range(n)]

print(string)
print([string for string in string if word in string])