#유기농 배추 

#input 
T = int(input())
# T=1
for i in range(T): 
    M,N,K = list(map(int,input().split()))
    bat = [[0]*M for _ in range(N)]  # 1. M * N 2차원 배열을 0으로 초기화하고 
    #input array 
    for _ in range(K): 
        i,j=map(int,input().split())
        bat[j][i]=1  #   1.1 . for문 돌면서 해당 자리를 1로 바꿔줌 

    #visit array ad
    di=[-1,1,0,0] # 상하 
    dj=[0,0,-1,1] # 좌우

    tmp=0
    cnt=0

    #바꿔준  array를 돌기 
    while K == 0:  # 배추의 개수가 0이 될때까지 
         i,j,dr=0,0,0  #현재자리 행, 열, 초기화 
         ni,nj = i+di[dr],j+dj[dr] #다음 자리 탐색 
         if 0<ni<N and  0<=nj<M and bat[ni][nj] == 1: # 배추 밭 범위안이거나 배추가 있는 부분 
              i,j=ni,nj #인접한 배추로 가는거임 
              K-=1 
              tmp+=1
         else: # 배추가 없을때 
             dr = (dr+1)%4 # 방향 순환

    print(tmp)

    