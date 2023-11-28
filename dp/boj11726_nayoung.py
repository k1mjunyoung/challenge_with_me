# https://www.acmicpc.net/problem/11726
# **2xn 타일링 

# output: 2xn 크기의 직사각형을 채우는 방법수 % 10,007 
'''
1. 도출한 점화식 
tile[1] =1 
tile[2] =2 
tile[n] = tile[n-2] + tile[n-1] 

'''
n=int(input()) 
tile = [-1]*10001
tile[1]=1 
tile[2]=2

for i in range(3,n+1): 
   tile[i] = tile[i-2] + tile[i-1] 

print(tile[n]%10007)

   



