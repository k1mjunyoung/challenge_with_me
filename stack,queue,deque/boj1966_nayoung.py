# https://www.acmicpc.net/problem/1966
# 프린터 큐 

'''
1. input() 
 1.1 testcase 개수 
 1.2 N 문서개수 
 1.3 index 인덱스 
 1.4 중요도가 주어진다. 


2. 프린트 작업  
2.1 queue[0] 을 뒤에 queue element 들과 비교 
    if queue[0]<queue[1] 이라면, element = queue[0] 저장 
    queue.popleft() 히고 queue.append(element) 
2.2  else 

ex) 중요도가 1 2 3 4 인 문서 4개가 있을 때 queue[2] 문서가 몇번째로 출력되는지 
'''

from collections import deque 


test_case = int(input())  # 문서의 개수 
for i in range(test_case): 
    N,M = map(int,input().split()) 
    queue = deque(map(int,input().split())) 

    #문서의 순서를 나타내는 리스트 생성 
    indices = list(range(N)) 
    indices[M] = 'target' 

    count = 0  #출력된 문서의 개수 
    while True: 
        if queue[0] == max(queue):
            count +=1 

            if indices[0] == 'target': 
                break 
            else: 
                queue.popleft() 
                indices.pop(0) #indices 의 첫번째 원소를 제거하고 반환 
        else: 
            queue.append(queue.popleft()) 
            indices.append(indices.pop(0))

 

    print(count)




