# 1. read input data and convert data types
yard_area = float(input())
# 2. Calculate total cost money needed
cost_per_sq_meter = 7.61
total_money_needed = yard_area * cost_per_sq_meter
# 3. Calculate 18% discount
discount = total_money_needed * 0.18
# 4. Calculate money needed without discount
final_cost = total_money_needed - discount
# 5. Print and format
print(f'The final price is: {final_cost:.2f} lv.')
print(f'The discount is: {discount:.2f} lv.')