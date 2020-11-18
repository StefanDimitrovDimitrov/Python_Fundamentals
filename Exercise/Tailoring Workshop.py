tables = int(input())
length = float(input())
width = float(input())

a_table_sheet = (length + 2 * 0.30)
b_table_sheet = (width + 2 * 0.30)

c_square = (length/2)

area_sheet = tables * (a_table_sheet * b_table_sheet)
area_square = tables * (c_square) * (c_square)

final_cost_USD = area_sheet * 7 + area_square * 9
final_cost_BGN = final_cost_USD * 1.85

print(f'{final_cost_USD: .2f} USD')
print(f'{final_cost_BGN: .2f} BGN')