# https://www.acmicpc.net/problem/10773
# 제로 
# 알고리즘 : 스택 
'''
1. input k 
2. 한줄에 하나씩 
2.1 if n==0 : pop()
    else : queue.append(n)
2.3 print(sum(queue))
'''
import sys 

K = int(sys.stdin.readline())
stack=[]
for i in range(K): 
    n=int(sys.stdin.readline())
    if n == 0:
        stack.pop()
    else: 
        stack.append(n) 


print(sum(stack))






