#문자열 집합 
#https://www.acmicpc.net/problem/14425
N,M = map(int,input().split())
# N개의 줄 : 집합 S에 포함되어 있는 문자열들이 주어짐 
# M개의 줄 : 검사해야 하는 문자열들이 주어짐 
s=[]
cnt=0 
for _ in range(N): 
    s.append(input()) 

for i in range(M): 
    tmp=input() 
    if tmp in s: # 해당 문자열이 s집합안에 있다면 
        cnt += 1 

print(cnt)



