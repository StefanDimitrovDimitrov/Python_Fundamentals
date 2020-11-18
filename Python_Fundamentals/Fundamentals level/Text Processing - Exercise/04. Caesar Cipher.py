


text = input()

result = []

for i in text:
    if i == "":
        continue
    else:
        num = ord(i) + 3
        result.append(chr(num))

print("".join(result))


