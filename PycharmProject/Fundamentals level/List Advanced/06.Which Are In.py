# words = input().split(', ')
#string = input()
#res_list = []

#for word in words:
    #if word in string:
      #  res_list.append(word)

#print(res_list)

words = input().split(', ')
string = input()
res_list = [word for word in words if word in string]

print(res_list)