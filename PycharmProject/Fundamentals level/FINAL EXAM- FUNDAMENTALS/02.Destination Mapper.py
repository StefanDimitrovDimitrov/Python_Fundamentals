import re
lenght = 0

pattern = r"(=|\/)([A-Z][A-Za-z]{2,})(\1)"

string = input()

matches = re.findall(pattern, string)

destinations = []

for match in matches:
    destinations.append(match[1])

result = ", ".join(destinations)

for n in destinations:
    lenght += len(n)

print(f"Destinations: {result}")

print(f"Travel Points: {lenght}")