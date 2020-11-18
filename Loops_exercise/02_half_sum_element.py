import sys

max_num = 0
max_num = -sys.maxsize
sum_number = 0

n = int(input())

for i in range(0, n):
    num = int(input())

    if num > max_num:
        max_num = num
    sum_number += num

sum_number -= max_num

if sum_number == max_num:
    print("Yes")
    print(f'Sum = {sum_number}')
else:
    print("No")
    print(f'Diff = {abs(max_num - sum_number)}')
