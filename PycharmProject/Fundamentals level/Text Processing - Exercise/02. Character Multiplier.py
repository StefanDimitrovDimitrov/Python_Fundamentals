text = input()

first_word, second_word = text.split()

min_lenght = min(len(first_word), len(second_word))

total_sum = 0

for i in range(min_lenght):
    result = ord(first_word[i]) * ord(second_word[i])
    total_sum += result

biggest_word = first_word

if len(second_word) > len(first_word):
    biggest_word = second_word

for i in range(min_lenght, len(biggest_word)):
    total_sum += ord(biggest_word[i])

print(total_sum)