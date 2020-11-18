factor = int(input())
count = int(input())

my_list = []
for num in range(factor, count*factor+1, factor):
   my_list.append(num)

print(my_list)

# my_list =[num **2 for num in range(factor,count*factor+1, factor)]

