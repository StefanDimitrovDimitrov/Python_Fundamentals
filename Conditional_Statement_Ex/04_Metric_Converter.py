number = float(input())
unit = str(input())
convert = str(input())

result = 0

if unit == "m" and convert == "cm":
    result = number * 100
elif unit == 'm' and convert == "mm":
    result = number * 1000
elif unit == 'cm' and convert == "m":
    result = number * 0.01
elif unit == 'cm' and convert == "mm":
    result = number * 10
elif unit == 'mm' and convert == "m":
    result = number * 0.001
elif unit == 'mm' and convert == "cm":
    result = number * 0.1

print(f'{result: .3f}')
