#https://www.acmicpc.net/problem/17626
#Four Squares 
# 알고리즘 : dp 

# import math 

# def ranglaju(x):
#     cnt = 0
#     while True:
#         tmp = int(math.sqrt(x))
#         num = x - (tmp ** 2)
#         cnt += 1
#         if num <= 1:
#             print(cnt)
#             break
#         x = num 

# n = int(input())
# ranglaju(n)


import math
 
n = int(input())
dp = [0,1]
 
for i in range(2, n+1):
    minValue = 1e9
    for j in range(1, int(math.sqrt(i)) + 1):
        minValue = min(minValue, dp[i - j**2])
    dp.append(minValue + 1)
 
print(dp[n])