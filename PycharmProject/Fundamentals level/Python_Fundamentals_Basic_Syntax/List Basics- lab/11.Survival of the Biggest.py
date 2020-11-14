list = list(map(int,input().split()))
n = int(input())

counter = 0

while counter < n:
    number = 99999999
    for i in list:
        if i < int(number):
            number = i

    list.remove(number)
    counter += 1

print(list)