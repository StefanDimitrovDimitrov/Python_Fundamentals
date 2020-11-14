def exchange(area, index_one):
    new_list = []

    new_list = area[int(index_one) + 1:]
    a = new_list + area[:int(index_one) + 1]

    return a


def first_last_odd_even(area, criteria_num, criteria_odd_even, first_or_last):
    temp_area = area
    new_list = []
    if int(criteria_num) > len(area):
        return "Invalid count"
    else:
        if first_or_last == "last":
            temp_area = list(reversed(area))

        for i, x in enumerate(temp_area):
            if x % 2 != 0 and criteria_odd_even == "odd":
                new_list.append(x)
            if x % 2 == 0 and criteria_odd_even == "even":
                new_list.append(x)
            # if int(criteria_num) - 1 == i:
            #     break

        if first_or_last == "last":
            return list(reversed(new_list[:int(criteria_num)]))
        else:
            return new_list[:int(criteria_num)]


def max_min_odd_even(area, criteria_max_min, criteria_odd_even):
    odd_max_num = 99999999

    even_max_num = 9999999

    odd_min_num = - 9999999

    even_min_num = - 9999999

    current_odd_max_index = 0
    current_odd_min_index = 0
    current_even_max_index = 0
    current_even_min_index = 0
    count_odd = 0
    count_even = 0
    result = 0

    for i, number in enumerate(area):
        if number % 2 != 0 and criteria_odd_even == "odd" and criteria_max_min == "max":
            count_odd += 1
            if number >= odd_min_num:
                odd_min_num = number
                current_odd_max_index = i
                result = current_odd_max_index
        elif number % 2 != 0 and criteria_odd_even == "odd" and criteria_max_min == "min":
            count_odd += 1
            if number <= odd_max_num:
                odd_max_num = number
                current_odd_min_index = i
                result = current_odd_min_index
        elif number % 2 == 0 and criteria_odd_even == "even" and criteria_max_min == "max":
            count_even += 1
            if number >= even_min_num:
                even_min_num = number
                current_even_max_index = i
                result = current_even_max_index
        elif number % 2 == 0 and criteria_odd_even == "even" and criteria_max_min == "min":
            count_even += 1
            if number <= even_max_num:
                even_max_num = number
                current_even_min_index = i
                result = current_even_min_index

    if criteria_odd_even == "odd" and count_odd == 0 or criteria_odd_even == "even" and count_even == 0:
        return "No matches"
    else:
        return result


area_one = input().split(" ")
area = list(map(int, list(area_one)))

while True:

    command = input()
    if command == 'end':
        break

    instruction = command.split(" ")[0]
    index_one = command.split(" ")[1]

    if instruction == "exchange" and abs(int(index_one)) < len(area):
        area = exchange(area, index_one)
    elif instruction == "exchange" and abs(int(index_one)) >= len(area):
        print("Invalid index")

    if instruction == "max" or instruction == "min":
        print(max_min_odd_even(area, instruction, index_one))

    if instruction == "first" or instruction == "last":
        index_two = command.split(" ")[2]
        print(first_last_odd_even(area, int(index_one), index_two, instruction))



print(area)