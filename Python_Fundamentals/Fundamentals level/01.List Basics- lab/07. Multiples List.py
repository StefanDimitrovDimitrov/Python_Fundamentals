"""
Write a program that receives two numbers (factor and count)
and creates a list with length of the given count
and contains only elements that are multiples of the given factor

"""

factor = int(input())
count = int(input())

my_list = []
for num in range(factor, count*factor+1, factor):
   my_list.append(num)

print(my_list)

# my_list =[num **2 for num in range(factor,count*factor+1, factor)]

