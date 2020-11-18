import math

N1 = int(input())
N2 = int(input())
operator = (input())

result = 0
type = ""

if operator == "+" and (N1 + N2) % 2 == 0:
    type = "even"
elif operator == "-" and (N1 - N2) % 2 == 0:
    type = "even"
elif operator == "*" and (N1 * N2) % 2 == 0:
    type = "even"
else:
    type = "odd"

if operator == "+":
    print(f' {N1} {operator} {N2} = {N1 + N2} - {type}')
elif operator == "-":
    print(f' {N1} {operator} {N2} = {N1 - N2} - {type}')
elif operator == "*":
    print(f' {N1} {operator} {N2} = {N1 * N2} - {type}')

if operator == "/" and N2 != 0:
    print(f'{N1} {operator} {N2} ={N1 / N2: .2f}')
elif operator == "%" and N2 != 0:
    print(f'{N1} {operator} {N2} = {N1 % N2}')
elif operator == "/" or operator == "%" and N2 == 0:
    print(f'Cannot divide {N1} by zero')
