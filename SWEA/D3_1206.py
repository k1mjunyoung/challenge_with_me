#[s/w 문제 해결 기본] 1일차 - View 


'''
0 0 3 5 2 4 9 0 6 4 0 8 0 0 

건물의 개수이므로 


1. t[2]빌딩 조망 확보 못함 -> 이유 : t[1]<t[2] , t[2]<t[3] 
 1.1 조건 1: t[n-1]<t[n]>t[n+1] 일때는 1차 조망확보 


2. 조건 2 : t[n-2]<t[n]>t[n+2]

3. true 한것의 인덱스 값을 구해서 list에 저장해서 
4. tmp = max(t[i-2],tt[i-1],t[i+1],t[i+2]) 한것에서 
5. tmp-t[i] 의 절대값을 total에 더하기 

'''

for test_case in range(1,11): 
    N=int(input()) 
    total=0
    buildings = list(map(int,input().split()))
    for i in range(2,len(buildings)-2): 
        if (buildings[i-1]<buildings[i]) and (buildings[i]>buildings[i+1]):
          if (buildings[i-2]<buildings[i]) and (buildings[i]>buildings[i+2]):
             tmp = max(buildings[i-2],buildings[i-1],buildings[i+1],buildings[i+2]) 
             cnt = abs(buildings[i]-tmp)
             total+=cnt


    print("#{} {}".format(test_case,total))






