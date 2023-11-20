# 파리퇴치 
# input 

T = int(input())
for testcase in range(1,T+1): 
    N,M = map(int,input().split()) 
    arr =[list(map(int,input().split())) for _ in range(N)]# 2차원 리스트 초기화 
    kills = []
    #파리채를 내려칠 곳 탐색 
    for i in range(N-M+1): 
        for j in range(N-M+1): 
            fly=0 
            #해당 위치를 타격했을 때 잡을 수 있는 파리의 수 탐색 
            for k in range(M): 
                 for l in range(M): 
                      fly+=arr[i+k][j+l]
            kills.append(fly)         


    print("#{} {}".format(testcase,max(kills)))



