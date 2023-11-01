# 백만 장자 프로젝트 
# 리스트를 거꾸로 체크하는 방식 
# algorithm type : greedy 

#input 
t = int(input()) # testcase 
for i in range (1,t+1): 
    N = int(input()) # N 일 
    tmp = list(map(int,input().split())) # 매매가 
    max_price = 0 # 현재 판매가격 (최대값) 
    v=0
    for j in tmp[::-1]: # 베열 거꾸로 순회 
        if (j>=max_price): # 현재 배열 인덱스가 최대값보다 크거나 같으면 
            max_price = j # 최대값 업데이트 
        else: 
            v +=max_price - j  # 그렇지않으면 최대값 - 현재값 
            
    print("#"+str(i),str(v)) 
    # print("#{} {}" .format(i,v)) # format 함수 사용 출력 


        
                

'''
 1. input()을 받을때 스택에 넣다가 
    1.1 if tmp[i]>tmp[i+1]: true면  s에 
  
t(1) 
1- 1 [2]
2- 2 [1] 
3- 3 
max_sum = 3 

t(2) 
1- 10 
2- 7 
3- 6 
max_sum = 0 [tmp[]]

t(3) 
1-3 [6]
2-5 [4] 
3-9 
max_sum = 10 

t(4) 
1-1 [2]
2-1 [2] 
3-3 [==4] 
4-1 [1] 
5-2
max_sum = 5 



'''