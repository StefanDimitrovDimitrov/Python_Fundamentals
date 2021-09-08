list_of_nums = list(map(int,input().split(", ")))

a = list_of_nums
max_value = []
boundary_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
last_boundary = 0
output_strings = []

for boundary in boundary_list:

    for i,item in enumerate(list_of_nums):

        if (boundary - 10) < item <= boundary:
            max_value.append(item)
            last_boundary = boundary

    output_strings.append( f"Group of {boundary}'s: {max_value}")
    max_value = []

# print
for i,boundary in enumerate(boundary_list):
    if last_boundary >= boundary:
        print(output_strings[i])

# list_of_nums = list(map(int, input().split(", ")))
#
# a = list_of_nums[:]
# max_value = []
# boundary_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# last_boundary = 0
# # output_strings = []
#
# for boundary in boundary_list:
#
#     for i, item in enumerate(a):
#
#         if (boundary - 10) < item <= boundary:
#             max_value.append(item)
#             list_of_nums.remove(item)
#
#     print(f"Group of {boundary}'s: {max_value}")
#     max_value = []
#
#     if list_of_nums == []:
#         break
