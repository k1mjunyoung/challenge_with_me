#최소힙 
#https://www.acmicpc.net/problem/1927


import heapq
import sys

arr_heap = []  # 최소 힙 초기화
N = int(input())  # 연산의 개수

for _ in range(N):
    n = int(sys.stdin.readline())
    
    if n > 0:
        heapq.heappush(arr_heap, n)  # 양수일 경우 최소 힙에 원소 추가
    elif n == 0:
        if not arr_heap:
            print(0)
        else:
            print(heapq.heappop(arr_heap))  # 최소 힙에서 원소를 뽑아서 출력




# arr_list = [] # 배열 초기화 
# N = int(input()) #연산의 개수 
# for i in range(N): 
#     n = int(sys.stdin.readline()) 
#     if n > 0: 
#         arr_list.append(n) 
#         arr_list.sort() #오름차순 정렬 
#     elif n==0: 
#         if len(arr_list)==0: 
#             print(0) 
#         else:
#             print(arr_list[0]) 
#             arr_list.remove(arr_list[0]) 



'''
1. 자연수 입력받기 
1.1 if x가 자연수 : arr_list.append(x) 
1.2 elif x가 0 : arr_list.remove(min(arr_list)) 
1.2.1 if arr_list.length =0 : print 0 

'''

