def smallest_number(first, second, third):
    if first < second and first < third:
        return first
    elif second < first and second < third:
        return second
    else:
        return third


first = int(input())
second = int(input())
third = int(input())

print(smallest_number(first, second, third))
