def sum_odd_even(text):
    odd_sum = 0
    even_sum = 0

    for ch in text:
        num = int(ch)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return f" Odd sum = {odd_sum}, Even sum = {even_sum}"

text = input()

res = sum_odd_even(text)

print(res)

