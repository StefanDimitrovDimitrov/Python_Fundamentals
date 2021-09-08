"""
You will be given a number n. On the next n lines you will receive integers. You have to create and print two lists:
•	One with all the positives (including 0)
•	One with all the negatives
Finally print the following message: "Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}"

"""

n = int(input())

positives = []
negatives = []

for n in range(n):
    current_number = int(input())
    positives.append(current_number) if current_number >= 0 else negatives.append(current_number)

print(f'{positives}')
print(f'{negatives}')
print(f'Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}')
