first_string = str(input())
second_string = str(input())

for i in range(len(first_string)):
    if first_string[i] != second_string[i]:
        for second_string_i in range(0, i + 1):
            print(second_string[second_string_i], end="")

        for first_string_i in range(i + 1, len(first_string)):
            print(first_string[first_string_i], end="")

        print()