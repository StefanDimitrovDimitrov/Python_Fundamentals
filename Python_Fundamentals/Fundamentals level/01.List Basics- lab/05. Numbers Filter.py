"""
You will receive a single number n. On the next n lines you will receive integers. After that you will be given one of the following commands:
•	even
•	odd
•	negative
•	positive
Filter all the numbers that fit in the category (0 counts as a positive). Finally, print the result
Input	Output
5
33
19
-2
18
998
even	[-2, 18, 998]
3
111
-4
0
negative	[-4]


"""




FILTERS_MAP = {

    'even': lambda number: number % 2 == 0,
    'odd': lambda number: number % 2 != 0,
    'positive': lambda number: number >= 0,
    'negative': lambda number: number < 0,
}

n = int(input())
numbers = [int(input()) for _ in range(n)]

filter_fn = FILTERS_MAP[input()]
print([n for n in numbers if filter_fn(n)])


