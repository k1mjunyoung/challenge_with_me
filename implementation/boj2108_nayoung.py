#https://www.acmicpc.net/problem/2108
#통계학 

'''
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
'''

import sys 
N =int(input())
stack=[]
for i in range(N):
    stack.append(int(sys.stdin.readline()))

stack.sort() 
def rangeto_stack(stack): 
    stack.sort() 
    if len(stack)==1:
        return print(0) 
    else: 
        r = stack[-1]-stack[0]
        return print(r)


#최빈값 구하는 함수 
def frequency_num(stack): 
    if len(stack)==1:
        return print(stack[0])
    else: 
        dic={}
        for value in stack:
            if value in dic:
                dic[value]+=1 
            else:
                dic[value] =1 
        mx = max(dic.values()) # 빈도수 중 최대값 구하기 
        mx_dic = [] 
        for i in dic:
            if mx ==dic[i]: # 최빈값의 key저장 
                mx_dic.append(i) 
        if len(mx_dic)>1:
            return print(mx_dic[1])
        else:
            return print(mx_dic[0])

# output 
print(round(sum(stack)/N)) #산술평균, 첫째자리 반올림 
print(stack[len(stack)//2]) #중앙값
frequency_num(stack) #최빈값중 두번째로 작은값 
rangeto_stack(stack) #범위 


'''
최빈값을 어떻게 구하더라...

count() 함수로 각 element의 빈도수를 구할수 있음 
1 2 2 3 4 
1. list(key=element, value=count)

2. value값으로 오름차순 
3. list[1].key값을 출력한다. 
'''




