# def first_factorial(first_num):
#     factorial = 1
#     for i in range(1,first_num+1):
#         factorial *= i
#     return factorial
#
#
# def second_factorial(second_num):
#     factorial = 1
#     for i in range(1,second_num + 1):
#         factorial *= i
#     return factorial
#
#
# first_num = int(input())
# second_num = int(input())
#
# result = first_factorial(first_num)/second_factorial(second_num)
#
# print(f"{result:.2f}")

def factorial(first_num, second_num):
    factorial_first = 1
    factorial_second = 1

    for i in range(1,first_num+1):
        factorial_first *=i

    for i in range(1,second_num+1):
        factorial_second *=i

    result = factorial_first/factorial_second

    return result


first_num = int(input())
second_num = int(input())

print(f'{factorial(first_num,second_num): .2f}')