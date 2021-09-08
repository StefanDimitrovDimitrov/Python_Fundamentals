def exchange(area, index_one):
    new_list = []

    new_list = area[int(index_one) + 1:]
    a = new_list + area[:int(index_one) + 1]

    return a

def last_odd_even(area, criteria_num, criteria_odd_even):

    new_list = []
    counter = 0
    temp_area = list(reversed(area))

    for i, x in enumerate(temp_area):
        if x % 2 != 0 and criteria_odd_even == "odd":
            new_list.append(x)
            counter += 1
            if int(criteria_num) == counter:
                break
        if x % 2 == 0 and criteria_odd_even == "even":
            new_list.append(x)
            counter += 1
            if int(criteria_num) == counter:
                break

    return list(reversed(new_list))

def first_odd_even(area, criteria_num, criteria_odd_even):
    temp_area = area
    new_list = []
    counter = 0

    for i, x in enumerate(temp_area):
        if x % 2 != 0 and criteria_odd_even == "odd":
            new_list.append(x)
            counter += 1
            if int(criteria_num) == counter:
                break
        if x % 2 == 0 and criteria_odd_even == "even":
            new_list.append(x)
            counter += 1
            if int(criteria_num) == counter:
                break

    return new_list

def min_odd_even(area, criteria_odd_even):
    max_num = 9999999
    current_index = -1

    for i, number in enumerate(area):
        if number % 2 != 0 and criteria_odd_even == "odd":
            if number <= max_num:
                max_num = number
                current_index = i


        elif number % 2 == 0 and criteria_odd_even == "even":
            if number <= max_num:
                max_num = number
                current_index = i

    if current_index == -1:
        return "No matches"
    else:
        return current_index

def max_odd_even(area, criteria_odd_even):

    min_num = -9999999
    current_index = -1

    for i, number in enumerate(area):
        if number % 2 != 0 and criteria_odd_even == "odd":
            count_odd = 1
            if number >= min_num:
                min_num = number
                current_index = i


        elif number % 2 == 0 and criteria_odd_even == "even":
            count_even = 1
            if number >= min_num:
                min_num = number
                current_index = i


    if current_index == -1:
        return "No matches"
    else:
        return current_index


area_one = input().split(" ")
area = list(map(int, list(area_one)))

while True:

    command = input()
    if command == 'end':
        break

    instruction = command.split(" ")[0]
    index_one = command.split(" ")[1]

    if instruction == "exchange":
        if abs(int(index_one)) < len(area) and int(index_one) >= 0:
            area = exchange(area, index_one)
        else:
            print("Invalid index")
    elif instruction == "max":
        print(max_odd_even(area, index_one))
    elif instruction == "min":
        print(min_odd_even(area, index_one))
    elif instruction == "first":
        index_two = command.split(" ")[2]
        if int(index_one) > len(area):
            print("Invalid count")
        else:
            print(first_odd_even(area, int(index_one), index_two))
    elif instruction == "last":
        index_two = command.split(" ")[2]
        if int(index_one) > len(area):
            print("Invalid count")
        else:
            print(last_odd_even(area, int(index_one), index_two))


print(area)