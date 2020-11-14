import re

pattern = "\d+"

while True:
    text = input()

    if not text:
        break

    res = re.findall(pattern, text)

    for r in res:
        print(r, end=" ")