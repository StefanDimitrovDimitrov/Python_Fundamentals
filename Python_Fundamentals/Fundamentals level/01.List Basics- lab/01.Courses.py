"""
You will receive a single number n. On the next n lines you will receive names of courses.
You have to create a list of them and print it

"""

n = int(input())

t = [input() for _ in range(n)]

print(t)
