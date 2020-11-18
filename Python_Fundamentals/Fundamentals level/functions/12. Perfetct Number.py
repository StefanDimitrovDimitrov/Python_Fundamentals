def is_perfect(number):

    result = 0
    for i in range(1,number):
        if number % i == 0:
            result += i

    return True if result == number else False

number = int(input())

if is_perfect(number):
    print("We have a perfect number!")
else:
    print( "It's not so perfect.")

