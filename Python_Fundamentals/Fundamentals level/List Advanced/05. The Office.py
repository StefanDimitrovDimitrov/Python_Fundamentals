employee_happiness = [int(happiness) for happiness in input().split()]
factor = int(input())

factor_employee_happiness = list(map(lambda h: h + factor, employee_happiness))
average_happiness = sum(factor_employee_happiness)/ len(factor_employee_happiness)
happy_employees = [e for e in factor_employee_happiness if e >= average_happiness]
unhappy_employees =[e for e in factor_employee_happiness if e < average_happiness]

if len(happy_employees) >= len(unhappy_employees):
    print(f'Score: {len(happy_employees)}/{len(employee_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(happy_employees)}/{len(employee_happiness)}. Employees are not happy!')