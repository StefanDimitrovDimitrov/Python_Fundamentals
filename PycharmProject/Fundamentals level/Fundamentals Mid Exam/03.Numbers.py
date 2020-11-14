numbers = list(map(int, input().split()))

average_number = sum(numbers) / len(numbers)

numbers = [x for x in numbers if x > average_number]

if not numbers:
    print("No")
else:
    numbers = (sorted(numbers, reverse =True))
    numbers = [str(n) for n in numbers]
    print(" ".join(numbers[:5]))
