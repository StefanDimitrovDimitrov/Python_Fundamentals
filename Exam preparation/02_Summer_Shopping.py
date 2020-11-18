budget = float(input())
price_beach_towel = float(input())
discount = float(input())

umbrela = price_beach_towel * 2/3
flip_flops = umbrela * 0.75
beach_bag = (price_beach_towel + flip_flops) / 3

final_discount = (umbrela + flip_flops + beach_bag + price_beach_towel) * discount /100
total = (umbrela + flip_flops + beach_bag + price_beach_towel) - final_discount

if total <= budget:
    print(f"Annie's sum is{total: .2f} lv. She has{budget - total: .2f} lv. left.")
else:
    print(F"Annie's sum is{total: .2f} lv. She needs{total - budget: .2f} lv. more.")
