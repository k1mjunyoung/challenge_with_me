#최빈수 구하기 


# t = int(input()) 
# # input data 1000개, 시간 : 10s 
# for i in range(t): 
#     n = int(input()) # 테스트 케이스 번호 
#     arr =[0]*1000 
#     for _ in range(1000):
#         tmp = int(input())
#         arr[tmp] +=1 
#     sum = max(arr) 
#     print("#{} {}".format(i,sum))



t = int(input()) 
# input data 1000개, 시간 : 10s 
for i in range(t): 
    n = int(input()) # 테스트 케이스 번호 
    arr =[0]*10 
    for i in range(10):
        tmp = int(input()) 
        arr[tmp] +=1 
    sum = max(arr) 
    print("#{} {}".format(i,sum))

