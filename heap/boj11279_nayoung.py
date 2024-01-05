# https://www.acmicpc.net/problem/11279
# 최대힙 

import sys 
import heapq 

heaplist =[] 
N = int(sys.stdin.readline()) 
for i in range(N): 
    n = int(sys.stdin.readline())
    if n >0:
        heapq.heappush(heaplist,-n)
    elif n==0: 
        if not heaplist: 
            print(0) 
        else: 
            print(-heapq.heappop(heaplist)) 


