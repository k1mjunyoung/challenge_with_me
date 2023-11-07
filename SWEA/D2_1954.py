#달팽이 숫자 
# algorithm type : 2차원 배열 리스트  - 다중 리스트 좌표개념  
'''
초기 :  i=0.j=0,cnt=1 arr[i][j] = cnt.cnt+=1 
while cnt<=N*N : # 범위 이내인 경우 
다음 위치 계산 : ni, nj 
di = [0,1,0,-1] dj =[1,0,-1,0]
dr = 0
ni = i+di[dr] 
dj = j+dj[dr]
if 0<=ni<N and 0<=nj<N  and anrr[ni]]nj] == 0 인 경우 해당 
좌표이동 : i,j = ni,nj  arr[i][j]=cnt cnt+=1 
else dr = (dr +1) % 4 


import sys 
sys.stdin= open("input.txt","r") 


'''

#input() 
T = int(input()) 
# 달팽이의 이동방향 ; 우>하>좌>상 , 방향 전환 리스트를 만들어준다. 
di = [0,1,0,-1]
dj = [1,0,-1,0]

for  test_case in range(1,T+1): 
    N = int(input())
    arr = [[0]*N for _ in range(N)] # 2차원 배열 초기화 list conprehension 
    i,j,cnt,dr=0,0,1,0  #초기화
    arr[i][j] = cnt
    cnt +=1 

    while cnt <= N*N: # 적을 값이 범위 이내라면 
        ni,nj = i+di[dr],j+dj[dr] 
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0: 
            i,j= ni,nj  #좌표 이동 
            arr[i][j] = cnt 
            cnt +=1 
        else: 
            dr = (dr+1)%4 # 방향을 순환해서 돌아야하니까 
        
    
    print(f'#{test_case}')
    for list in arr:
        print(*list)
