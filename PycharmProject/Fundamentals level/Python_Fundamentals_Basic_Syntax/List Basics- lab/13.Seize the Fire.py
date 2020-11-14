# 1. Validate input
# 2. Check Water to a fire Amount
# 3. Calculate Water
# 4. Calculate Effort

def IsItInRange(type, value):
    if type == 'High' and value >= 81 and value <= 125:
        return True
    if type == 'Medium' and value >= 51 and value <= 80:
        return True
    if type == 'Low' and value >= 1 and value <= 50:
        return True

    return False


fire_list = input().split("#")
# print(fire_list)
water_amount = int(input())
effort = 0
list_cell_output = []
total_fire = 0
value_of_cell = 0

for pair in fire_list:
    type_of_fire = pair.split(" = ")[0]
    value_of_cell = int(pair.split(" = ")[1])

    if IsItInRange(type_of_fire, value_of_cell):
        if water_amount >= value_of_cell:
            water_amount -= value_of_cell
            total_fire += value_of_cell
            effort += float((25 / 100) * value_of_cell)
            list_cell_output.append(value_of_cell)


print("Cells:")

for cell in list_cell_output:
    print(f" - {cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
