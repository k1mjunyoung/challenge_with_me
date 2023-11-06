# 파리퇴치 
# input 
T = int(input())
for i in range(1,T+1): 
    N,M = map(input().split()) 

    dx = [1,-1,0,0]  #상하
    dy = [0,0,-1,1]  #좌우 