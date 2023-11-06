#최빈수 구하기 

t = int(input()) 
# input data 1000개, 시간 : 10s 
for i in range(1,t+1): 
    n = int(input()) # 테스트 케이스 번호 
    arr =[0]*11 # 빈도수를 저장할 리스트 초기화 
    tmp =  map(int,input().split())
    for K in tmp:
        arr[K] += 1 # 해당 인덱스에 +1 (빈도수) 
    frequency = max(arr) 
    # 리스트를 뒤집어서 찾기 
    reversed_arr = arr[::-1] 
    score = len(arr)-reversed_arr.index(frequency)-1 # 값을 알고 해당 위치찾기 
    
    print("#{} {}".format(i,score))
