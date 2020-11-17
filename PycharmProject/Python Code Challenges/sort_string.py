# # input - string 3 words
# # sort them a to z
# # return the same string
#
#
# def sort_string(word_colection):
#     final_list = []
#     new_masive = []
#     for word in word_colection:
#          new_masive.append(word.lower())
#     new_masive = sorted(new_masive)
#
#     for word in new_masive:
#         for word1 in word_colection:
#             if word.lower() == word1.lower():
#                 final_list.append(word1)
#     return final_list
#
#
# input_string = "bananabababnaorangeORANGE Appleapple"
# print(sort_string(input_string.split()))



def sort_words(input):
    words = input.split()
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    return ' '.join(words)

input = input()
print(sort_words(input))