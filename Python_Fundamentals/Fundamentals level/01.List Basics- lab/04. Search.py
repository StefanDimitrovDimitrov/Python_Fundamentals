"""

You will receive a number n and a word. On the next n lines you will be given some strings.
You have to add them in a list and print them.
After that you have to filter out only the strings that include the given word and print that list also

"""

n = int(input())
word = input()

string = [input() for _ in range(n)]

print(string)
print([string for string in string if word in string])