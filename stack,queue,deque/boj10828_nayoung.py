# https://www.acmicpc.net/problem/10828
# 스택 


# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys 
stack = [] 

N = int(input()) #testcase 
for i in range(N):
    tmp = sys.stdin.readline().split() 
    order = tmp[0] 
   
   
    if order == "push":
        element = int(tmp[1])
        stack.append(element)
    elif order == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif order == "top": 
        if not stack:
            print(-1) 
        else: 
            print(stack[-1])


