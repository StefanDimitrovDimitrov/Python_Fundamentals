price_U = float(input())
quantity_b = float(input())
quantity_w = float(input())
quantity_r = float(input())
quantity_u = float(input())

price_r = price_U / 2
price_w = price_r * 0.60
price_b = price_r * 0.20

money_of_whiskey = price_U * quantity_u
money_of_rakia = price_r * quantity_r
money_of_wine = price_w * quantity_w
money_of_beer = price_b * quantity_b

Total = money_of_whiskey + money_of_rakia + money_of_wine + money_of_beer

print(f'{Total: .2f}')