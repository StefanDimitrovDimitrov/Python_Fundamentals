from math import floor

l_of_the_hall = float(input())
w_of_the_hall = float(input())
a_wardrobe = float(input())

area_of_hall = l_of_the_hall * w_of_the_hall * 10000
area_of_wardrobe = a_wardrobe * a_wardrobe * 10000

bench = area_of_hall / 10

free_space = area_of_hall - area_of_wardrobe - bench

dancers = free_space / 7040

print(floor(dancers))
