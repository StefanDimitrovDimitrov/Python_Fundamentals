def even_odd(*args):
    x = 0 if args[-1] == "even" else 1
    return [num for num in args[:-1] if num % 2 == x]

print(even_odd(1, 2, 3, 4, 5, 6, "even"))