n = int(input())
even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum = even_sum + int(input())
    else:
        odd_sum = odd_sum + int(input())

if even_sum == odd_sum:
    print(f"Yes")
    print(f'Sum = {even_sum}')
else:
    print(f"No")
    print(f'Diff = {abs(even_sum - odd_sum)}')