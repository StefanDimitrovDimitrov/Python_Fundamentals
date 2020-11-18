income = int(input())
num_months = int(input())
monthly_outcomes = int(input())

money_saved = income * 0.3

savings = income - (monthly_outcomes + money_saved)

total_savings = savings * num_months

print(f'She can save {savings/income:.2%}')
print(f'{total_savings:.2f}')
