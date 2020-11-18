budjet_movies = float(input())
stats_number = int(input())
price_dressed = float(input())

decore = budjet_movies * 0.1
price_dressed = stats_number * price_dressed

if stats_number >150:
    price_dressed -= price_dressed * 0.1

expences = decore + price_dressed

if expences > budjet_movies:
    print('Not enough money!')
    print(F"Wingard needs{expences - budjet_movies: .2f} leva more.")

elif expences <= budjet_movies:
    print('Action!')
    print(f"Wingard starts filming with{budjet_movies - expences: .2f} leva left.")