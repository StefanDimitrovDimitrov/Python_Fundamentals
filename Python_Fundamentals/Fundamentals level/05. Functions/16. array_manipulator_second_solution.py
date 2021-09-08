"""
The array may be manipulated by one of the following commands
•	exchange {index} – splits the array after the given index, and exchanges the places of the two resulting sub-arrays. E.g. [1, 2, 3, 4, 5] -> exchange 2 -> result: [4, 5, 1, 2, 3]
o	If the index is outside the boundaries of the array, print "Invalid index"
•	max even/odd– returns the INDEX of the max even/odd element -> [1, 4, 8, 2, 3] -> max odd -> print 4
•	min even/odd – returns the INDEX of the min even/odd element -> [1, 4, 8, 2, 3] -> min even > print 3
o	If there are two or more equal min/max elements, return the index of the rightmost one
o	If a min/max even/odd element cannot be found, print "No matches"
•	first {count} even/odd– returns the first {count} elements -> [1, 8, 2, 3] -> first 2 even -> print [8, 2]
•	last {count} even/odd – returns the last {count} elements -> [1, 8, 2, 3] -> last 2 odd -> print [1, 3]
o	If the count is greater than the array length, print "Invalid count"
o	If there are not enough elements to satisfy the count, print as many as you can. If there are zero even/odd elements, print an empty array "[]"
•	end – stop taking input and print the final state of the array

"""


def exchange(list_nums, command):
    index = int(command.split(" ")[1])
    if index > len(list_nums) and index > 0:
        print("Invalid index")
        return list_nums
    else:
        list_nums = list_nums[index + 1:] + list_nums[:index + 1]
        return list_nums


def max_index(list_nums, command):
    def index_max_even(list_nums):
        max_even = [nums for nums in list_nums if nums % 2 == 0]
        if len(max_even) == 0:
            return "No matches"
        else:
            index_max_even = max([i for i, j in enumerate(list_nums) if j == max(max_even)])
            return index_max_even

    def index_max_odd(list_nums):
        max_odd = [nums for nums in list_nums if nums % 2 != 0]
        if len(max_odd) == 0:
            return "No matches"
        else:
            index_max_odd = max([i for i, j in enumerate(list_nums) if j == max(max_odd)])
            return index_max_odd

    tokken = command.split()[1]
    print(index_max_even(list_nums) if tokken == "even" else index_max_odd(list_nums))
    return list_nums


def min_index(list_nums, command):
    def min_even(list_nums):
        min_even = [nums for nums in list_nums if nums % 2 == 0]
        if len(min_even) == 0:
            return "No matches"
        else:
            index_min_even = max([i for i, j in enumerate(list_nums) if j == min(min_even)])
            return index_min_even

    def min_odd(list_nums):
        min_odd = [nums for nums in list_nums if nums % 2 != 0]
        if len(min_odd) == 0:
            return "No matches"
        else:
            index_min_odd = max([i for i, j in enumerate(list_nums) if j == min(min_odd)])
            return index_min_odd

    tokken = command.split()[1]
    print(min_even(list_nums) if tokken == "even" else min_odd(list_nums))
    return list_nums


def first_numbers(list_nums, command):
    def first_n_even(list_nums, count):
        even_numbers = [num for num in list_nums if num % 2 == 0]
        if len(even_numbers) < count:
            return even_numbers
        else:
            first_evens = even_numbers[:count]
            return first_evens

    def first_n_odd(list_nums, count):
        odd_numbers = [num for num in list_nums if num % 2 != 0]
        if len(odd_numbers) < count:
            return odd_numbers
        else:
            first_odds = odd_numbers[:count]
            return first_odds

    count = int(command.split()[1])
    tokken = command.split()[2]

    if count > len(list_nums):
        print("Invalid count")
    else:
        print(first_n_even(list_nums, count) if tokken == "even" else first_n_odd(list_nums, count))
    return list_nums


def last_numbers(list_nums, command):
    def last_n_even(list_nums, count):
        even_numbers = [num for num in list_nums if num % 2 == 0]
        if len(even_numbers) < count:
            return even_numbers
        else:
            last_evens = even_numbers[::-1][:int(count)]
            return last_evens

    def last_n_odd(list_nums, count):
        odd_numbers = [num for num in list_nums if num % 2 != 0]
        if len(odd_numbers) < count:
            return odd_numbers
        else:
            first_odds = odd_numbers[::-1][:int(count)]
            return first_odds

    count = int(command.split()[1])
    tokken = command.split()[2]
    if count > len(list_nums):
        print("Invalid count")
    else:
        print(last_n_even(list_nums, count) if tokken == "even" else last_n_odd(list_nums, count))
    return list_nums


list_nums = list(map(int, input().split(" ")))

commands = {
    'exchange': exchange,
    'max': max_index,
    'min': min_index,
    'first': first_numbers,
    'last': last_numbers,
}

while True:

    command = input()
    if command == "end":
        break

    key = command.split()[0]
    list_nums = commands[key](list_nums, command)

print(list_nums)
