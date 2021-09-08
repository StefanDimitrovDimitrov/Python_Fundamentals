food_money = int(input())
suv_money = int(input())
hotel_money = int(input())

money_traveling = (420 / 100 * 7) * 1.85
food_money = food_money * 3
suv_money = suv_money * 3

first_day_hotel_money = hotel_money * 0.9
secound_day_hotel_money = hotel_money * 0.85
tiird_day_hotel_money = hotel_money * 0.8

total_money = money_traveling + food_money + suv_money + first_day_hotel_money + secound_day_hotel_money + tiird_day_hotel_money

print(f"Money needed:{total_money: .2f}")
