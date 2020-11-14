import re

# pattern = r"(\@\#+)([A-Z]+([A-Za-z]*[0-9]*[A-Za-z]*){6}[A-Z])(\@\#+)"
pattern = r"(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(\@\#+)"


n = int(input())

for _ in range(n):

    line = input()

    match = re.fullmatch(pattern, line)

    if match is None:
        print("Invalid barcode")
    else:
        result = ''.join(c for c in match[2] if c.isdigit())

        if result == "":
            print("Product group: 00")
        else:
            print(f"Product group: {result}")
