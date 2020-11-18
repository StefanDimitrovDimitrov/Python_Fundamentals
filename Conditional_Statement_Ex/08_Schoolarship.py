from math import floor

income = float(input())
average_score = float(input())
min_salary = float(input())

soc_scholarship = 0
scholareship_hight_score = 0

if income < min_salary:
    if average_score > 4.5:
        soc_scholarship = min_salary * 0.35

if average_score >= 5.50:
    scholareship_hight_score = average_score * 25

if soc_scholarship > scholareship_hight_score:
        print(f'You get a Social scholarship {floor(soc_scholarship)} BGN')
elif scholareship_hight_score > soc_scholarship:
        print(f'You get a scholarship for excellent results {floor(scholareship_hight_score)} BGN')
else:
    print('You cannot get a scholarship!')



