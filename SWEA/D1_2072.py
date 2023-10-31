# 홀수만 더하기 
# 10개의 수를 입력받아, 홀수만 더한값 출력 
# output 형식 : 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력

t=int(input()) 
for test_case in range(1,t+1):
    li = list(map(int, input().split()))
    answer = 0
    for i in range(10):
        if li[i]%2!=0:
            answer += li[i]
    print("#"+str(test_case),str(answer))

'''
t = int(input())
 
for test_case in range(1,t+1):
    li = map(int, input().split())
    answer = 0
    for i in li:
        if i%2!=0:
            answer += i
    print("#"+str(test_case),str(answer))
'''

