#돌게임 
# https://www.acmicpc.net/problem/9655


# DP 이용 
n = int(input())
win = [-1]*10001
win[1] =1 # SK 가 이기면 1 
win[2] =0 # CY 가 이기면 0    
win[3] =1 

for i in range(4,n+1): 
    if win[i-1]==1 or win[i-3] ==1:
        win[i]=0 
    else: 
        win[i]=1 

if win[n]==1:
    print('SK')
else:
    print('CY') 



    

'''
#패턴을 찾아서 푼 풀이 
n=int(input()) 
if n % 2 == 0:
    print('CY')
else:
    print('SK')

'''






