#피보나치 함수 
# https://www.acmicpc.net/problem/1003



def fibonacci(n):
    global tmp 
    if n==0: 
        tmp.append(0)
        return 0
    elif n==1 or n==2:
        tmp.append(1) 
        return 1 
    elif d[n]!=0:
        return d[n] 
    else:
        d[n] = fibonacci(n-1) + fibonacci(n-2) 
        return d[n]



t = int(input()) 
for i in range(t): 
    n = int(input())
    zero_count,one_count=0,0
    d=[0]*100
    tmp=[]
    result = fibonacci(n)
    zero_count=tmp.count(0) 
    one_count=tmp.count(1) 
    print(zero_count,"",one_count)
  


