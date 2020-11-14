n = int(input())

count_a = 0
count_b = 0
index = 0
is_open_b = True

for i in range(n):
    string = input()

    if string == "(":
        count_a += 1
        index += 1

    if string == ")":
        count_b += 1
        index -= 1

    if index == 2 or index < 0:
        is_open_b = False
        break

if is_open_b and count_a == count_b:
    print("BALANCED")
else:
    print("UNBALANCED")
