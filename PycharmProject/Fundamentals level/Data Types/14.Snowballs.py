n = int(input())

snowball_value_current = 0
max = -9999999999
snow = 0
time = 0
quality = 0

for snowball in range(n):

    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value_current = int(snowball_snow / snowball_time) ** snowball_quality

    if snowball_value_current > max:
        max = snowball_value_current
        snow = snowball_snow
        time = snowball_time
        quality = snowball_quality

print(f'{snow} : {time} = {max} ({quality})')
