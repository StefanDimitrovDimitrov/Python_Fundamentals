Tabs_open = int(input())
salary = int(input())

for i in range(Tabs_open):
    name = input()
    if name == "Facebook":
        salary -= 150
    elif name == "Instagram":
        salary -= 100
    elif name == "Reddit":
        salary -= 50
    if salary <=0:
        break

if salary <= 0:
    print('You have lost your salary.')
else:
    print(salary)
