#달팽이 숫자 
# algorithm type : 2차원 배열 리스트  - 다중 리스트 좌표개념  

'''
상하 좌우 
dr = [-1,1,0,0]
dc = [0,0,-1,1]
'''

#input() 
t = int(input()) 
# 달팽이의 이동방향 ; 우>하>좌>상 , 방향 전환 리스트를 만들어준다. 
di = [0,1,0,-1]
dj = [1,0,-1,0]

for tc in range(1,t+1): 
    N = int(input())
    arr = [[0]*N for _ in range(N)] # 2차원 배열 초기화 

    i,j,cnt,dr=0,0,1,0  #초기화
    arr[i][j] = cnt
    cnt +=1 

    while cnt <= N*N:
        ni,nj = i+di[dr],j+dj[dr] 
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] ==0 : 
            i,j= ni,nj
            arr[i][j] = cnt 
            cnt +=1 

        else: 
            dr = (dr+1)%4
        
    
    print("#"+str(tc))
    for list in arr:
        print(*list)




# 방향 전환이 일어나기 전까지 값을 더한다. 
# row 나 column 인덱스가 범위 밖인 경우 or 이미 방문한(숫자가 입력된 상태) 일 경우 

