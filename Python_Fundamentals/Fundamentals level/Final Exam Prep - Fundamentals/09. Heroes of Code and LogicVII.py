from _collections import defaultdict
n = int(input())

heros = defaultdict(int)
for _ in range(n):

    hero_name,hit_points,mana_points = input().split()
    heros[hero_name] = [int(hit_points),int(mana_points)]


while True:

    command = input()

    if command == "End":
        break

    magic = command.split(" - ")[0]
    hero_name = command.split(" - ")[1]

    if magic == "CastSpell":
        mana_points_left = 0
        mp_needed = int(command.split(" - ")[2])
        spell_name = command.split(" - ")[3]
        if mp_needed <= heros[hero_name][1]:
            mana_points_left = heros[hero_name][1] - mp_needed
            heros[hero_name][1] = mana_points_left
            print(f"{hero_name} has successfully cast {spell_name} and now has {mana_points_left} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif magic == "TakeDamage":
        damage = int(command.split(" - ")[2])
        attacker = command.split(" - ")[3]
        heros[hero_name][0] -= damage
        if heros[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heros[hero_name][0]} HP left!")
        else:
            del heros[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
    elif magic == "Recharge":
        amount_recovered = int(command.split(" - ")[2])
        temp = heros[hero_name][1]
        heros[hero_name][1] += amount_recovered
        if heros[hero_name][1] > 200:
            amount_recovered = 200 - temp
            heros[hero_name][1] = 200
        print(f"{hero_name} recharged for {amount_recovered} MP!")

    elif magic == "Heal":
        amount_recovered = int(command.split(" - ")[2])
        temp = heros[hero_name][0]
        heros[hero_name][0] += amount_recovered
        if heros[hero_name][0] > 100:
            amount_recovered = 100 - temp
            heros[hero_name][0] = 100
        print(f"{hero_name} healed for {amount_recovered} HP!")


heros = dict(sorted(heros.items(), key= lambda x: (-x[1][0], x[0])))


for k,v in heros.items():
    print(k)
    print(f'  HP: {v[0]}')
    print(f'  MP: {v[1]}')