"""
Write a program that receives a single word from the user, reverses it and prints it
Example
Input	Output
Python	nohtyP
banana	ananab

"""


word = input()
word = word[::-1]
print(word)

# reversed_word = ""
#
# for i in range(len(word) - 1, -1, -1):
#     reversed_word += word[i]
# print(reversed_word)


