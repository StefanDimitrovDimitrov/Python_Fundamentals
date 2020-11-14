from collections import defaultdict

plant_rarity = defaultdict(int)
plant_ratings = defaultdict(int)
final_dic = {}
n = int(input())

for _ in range(n):
    plant, rarity = input().split("<->")

    plant_rarity[plant] = int(rarity)
    plant_ratings[plant] = []

while True:

    commands = input()

    if commands == "Exhibition":
        break

    action = commands.split(": ")[0]
    plant = commands.split(": ")[1].split(" - ")[0]

    if action == "Rate":
        ratings = int(commands.split(": ")[1].split(" - ")[1])
        plant_ratings[plant].append(ratings)
    elif action == "Update":
        new_rarity = int(commands.split(": ")[1].split(" - ")[1])
        plant_rarity[plant] = new_rarity
    elif action == "Reset":
        plant_ratings[plant] = []
    else:
        print("error")

for k, v in plant_ratings.items():
    if v == []:
        avr_points = 0
    else:
        avr_points = sum(v) / len(v)
    plant_ratings[k] = avr_points

for k in plant_rarity:
    final_dic[k] = plant_rarity[k], plant_ratings[k]

final_dic = dict(sorted(final_dic.items(), key=lambda x: (-x[1][0], -x[1][1])))

print(f"Plants for the exhibition:")

for k in final_dic.keys():
    print(f"- {k}; Rarity: {plant_rarity[k]}; Rating: {plant_ratings[k]:.2f}")
