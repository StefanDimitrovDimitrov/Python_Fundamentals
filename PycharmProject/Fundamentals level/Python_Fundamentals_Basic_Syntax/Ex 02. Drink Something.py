age = float(input())

drink = ""

if age > 21:
    drink = "drink whisky"
elif age > 18:
    drink = "drink beer"
elif age > 14:
    drink = "drink coke"
else:
    drink = "drink toddy"

print(f'{drink}')
