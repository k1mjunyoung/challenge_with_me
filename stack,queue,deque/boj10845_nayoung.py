# https://www.acmicpc.net/problem/10845
# 큐 
'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
from collections import deque
import sys
N = int(input())
queue = deque()

for i in range(N):
    tmp = sys.stdin.readline().split()
    order = tmp[0]

    if order == "push":
        element = int(tmp[1])
        queue.append(element)
    elif order == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif order == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif order == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])

        



 