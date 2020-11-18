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


