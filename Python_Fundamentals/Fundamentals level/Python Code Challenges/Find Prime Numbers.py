# import math
# def primeFactors(n):
#
#     while n % 2 == 0:
#         result.append(2),
#         n = n / 2
#
#     for i in range(3, int(math.sqrt(n))+1,2):
#
#         while n % i ==0:
#             result.append(i)
#             # print(i),
#             n = n / i
#
#     if n > 2:
#         print(n)
#
# result = []
#
# n = int(input())
# primeFactors(n)
#
# print(result)

def get_prime_factors(N):
    factors = []
    divisor = 2
    while(divisor <= N):
        if (N % divisor) == 0:
            factors.append(divisor)
            N = N/divisor
        else:
            divisor += 1
    return factors


n = int(input())
print(get_prime_factors(n))