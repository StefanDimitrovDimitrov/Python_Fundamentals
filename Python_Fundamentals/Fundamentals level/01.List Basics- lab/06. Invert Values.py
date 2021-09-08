"""
Write a program that receives a single string containing numbers separated by a single space.
Print a list containing the opposite of each number
"""

num_str = input().split()
nums = [-int(num) for num in num_str]

print(nums)

