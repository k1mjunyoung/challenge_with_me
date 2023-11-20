# 평균값 구하기 

t = int(input()) 
for i in range(1,t+1): 
    n = list(map(int,input().split()))
    tmp = sum(n) 
    avg = tmp / len(n) 

    print("#{} {}".format(i,round(avg)))
