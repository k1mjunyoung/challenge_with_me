#https://www.acmicpc.net/problem/2164
#카드2 
# 큐 

from collections import deque 
N = int(input())  
queue = deque() 

for i in range(1,N+1): 
    queue.append(i) 

    
while len(queue)>1: 
    queue.popleft() 
    new_element = queue[0]
    queue.popleft() 
    queue.append(new_element) 


print(queue[0])     

