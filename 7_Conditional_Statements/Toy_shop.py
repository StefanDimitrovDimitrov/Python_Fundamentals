vacation_price = float(input())
Number_puzzle = int(input())
Number_doll = int(input())
Number_bear = int(input())
Number_minions = int(input())
Number_trucks = int(input())

sum_p = Number_puzzle * 2.6
sum_d = Number_doll * 3
sum_b = Number_bear * 4.1
sum_m = Number_minions * 8.2
sum_t = Number_trucks * 2

total = sum_p + sum_d + sum_b + sum_m + sum_t
total *= 0.9

number_of_toies = Number_trucks + Number_minions + Number_bear + Number_doll + Number_puzzle

if number_of_toies >= 50:
    total *= 0.75

if total >= vacation_price:
    print(f"Yes! {total - vacation_price:.2f} lv left.")
else:
    print(f"Not enough money! {vacation_price - total:.2f} lv needed.")

#print(total)
