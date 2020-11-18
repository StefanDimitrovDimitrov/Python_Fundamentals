budget = float(input())
price_flour = float(input())

count = 0
current_budget = budget
count_cozonac = 0
count_eggs = 0
price_pack_of_egg = price_flour * 0.75
price_milk_250ml = (price_flour + price_flour * 0.25) / 4
price_cozonac = price_flour + price_pack_of_egg + price_milk_250ml

while current_budget > price_cozonac:
    current_budget -= price_cozonac
    count += 1
    count_cozonac += 1
    count_eggs += 3

    if count == 3:
        count_eggs -= count_cozonac - 2
        count = 0

print(f"You made {count_cozonac} cozonacs! Now you have {count_eggs} eggs and {current_budget:.2f}BGN left.")