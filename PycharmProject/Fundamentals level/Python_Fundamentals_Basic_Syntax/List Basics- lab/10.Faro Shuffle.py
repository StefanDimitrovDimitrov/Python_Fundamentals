def shufflist(new_list):
    a = int(len(new_list) / 2)
    left_card = new_list[:a]
    right_card = new_list[a:]
    shuffled_list = []

    for i in range(int(a)):
        shuffled_list.append(right_card[i])
        shuffled_list.append(left_card[i])


    return shuffled_list

my_list = input().split()

shuffles = int(input())

new_list = my_list[1:-1]
count = 0

while count < shuffles:

    new_list = shufflist(new_list)
    count += 1

new_list.insert(0,my_list[0])
new_list.append(my_list[-1])

print(f'{new_list}')
