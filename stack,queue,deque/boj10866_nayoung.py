#https://www.acmicpc.net/problem/10866
#덱
'''
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''


from collections import deque
import sys
N = int(input())
queue = deque()

for i in range(N):
    tmp = sys.stdin.readline().split()
    order = tmp[0]

    if order == "push_front":
        element = int(tmp[1])
        queue.appendleft(element) 
    elif order == "push_back": 
        element = int(tmp[1])
        queue.append(element) 
    elif order == "pop_front": 
        if not queue:
            print(-1) 
        else: 
            print(queue.popleft())
    elif order == "pop_back":
        if not queue: 
            print(-1) 
        else:
            print(queue.pop()) 
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







