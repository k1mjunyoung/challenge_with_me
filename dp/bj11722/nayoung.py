# https://www.acmicpc.net/problem/11722
# ** 가장 긴 감소하는 부분수열 ** 


# 부분수열 ? 원래 시퀀스에서 일부 원소들을 선택하여 순서를 유지한 채로 만든 새로운 시퀀스 
# 감소하는 부분수열 ? [45,50,25,10,18,20] 이라는 수열이 있다고 가정하면, [45,25,10] 은 감소하는 부분수열
# output : 가장 긴 감소하는 부분수열의 길이

n = int(input()) 
nums = list(map(int,input().split()))
#dp배열 초기화 - 각 원소는 최소한 자신 하나만을 포함하는 길이 이므로 1로 초기화 
dp=[1]*n
#dp배열 갱신 
for i in range(n):
    for j in range(0,i): 
        if(nums[i]<nums[j]):
            dp[i]=max(dp[i],dp[j]+1) 
#최대 길이 출력 
print(max(dp))