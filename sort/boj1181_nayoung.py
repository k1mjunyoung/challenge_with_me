#단어정렬 
#https://www.acmicpc.net/problem/1181
#유사문제 boj1431

#길이가 짧은것부터 
#길이가 같으면 사전순으로 


''' 
lambda 를 이용한 정렬을 해보자 

'''
N = int(input())
verb =[]
for _ in range(N): 
    verb.append(input()) 

verb = list(set(verb))    #중복제거 set() 

verb.sort(key=lambda x:(len(x),x))
for i in verb: 
    print(i) 

