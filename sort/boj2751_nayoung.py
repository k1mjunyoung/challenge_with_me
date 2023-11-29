
# 수정렬하기2 
# https://www.acmicpc.net/problem/2751

# pytho3 - 시간 초과 
# pypy - 메모리 : 191668KB / 시간 : 904ms 
# sys 버전 - 메모리 : 76972KB / 시간 : 1400ms 

import sys 
ipt = sys.stdin.readline 
# N = int(input()) 
tmp =[] 
for i in range(int(ipt())): 
    tmp.append(int(ipt()))     
tmp.sort()
for j in tmp:
    print(j)

    