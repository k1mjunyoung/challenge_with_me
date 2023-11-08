# 부분수열 
# dp - 작은 부분으로 쪼개서 하는거기 때문에 ? 
# 5,3으로 나누기 
# 먼저 5로 쪼개고 3으로 쪼개기 남은 수가 3보다 작다면 -1 출력 


#input 
N=int(input())
cnt=0 # 봉지의 개수 

# 메모이제이션을 위한 딕셔너리 초기화 
d={}

def fibo(x): 
    if x==1 or x==2: 
        return -1 
    if x in d:
        return d[x]
    
    d[x] = 1+min(fibo(x-5),fibo(x-3))
    return d[x]
 

result = fibo(N)

if result <0: 
    print(result)
else:
    print(result+cnt)



# if 이 N이 5,3으로 이루어진 합이 만들어지는지 확인 
# else -1 
# TOP-DOWN방식 이용 
# 점화식이 필요 ? 
# n을 5,3으로 찢을수있는 모든 경우의수 찾기 그중 리스트.length가 가장 작은 수만 
d =[0]*100