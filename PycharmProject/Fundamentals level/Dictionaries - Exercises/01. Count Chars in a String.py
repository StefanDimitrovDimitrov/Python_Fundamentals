from _collections import defaultdict

text = input()

occurrences = defaultdict(int)

for ch in text:
    if ch == " ":
        continue

    if ch in occurrences:
        occurrences[ch] += 1
    else:
        occurrences[ch] = 1

for key, value in occurrences.items():
    print(f"{key} -> {value}")
