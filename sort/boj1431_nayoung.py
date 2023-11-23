#시리얼 번호 _s3 
# https://www.acmicpc.net/problem/1431

n = int(input()) 
def sum_num(inputs):  # 리스트에 있는 숫자들을 구하는 함수 
    result = 0
    for i in inputs:
        if i.isdigit():
            result+=int(i) 
    return result 


arr=[]
for i in range(n): 
    a = input() 
    arr.append(a) 

arr.sort(key=lambda x:(len(x),sum_num(x),x))
for i in arr:
    print(i) 



'''
모든 시리얼 번호 알파벳(대문자) + 숫자 
조건1. if a와b 길이 다르면, 짧은것이 먼저 
조건2. elif 서로 길이 같으면, a모든 자리수 합 , b모든 자리수합 적은합 먼저 (숫자인것만)
조건3. else: 사전순으로 비교, 알파벳 > 숫자 


#input 
N=int(input()) 

arr = [] #answer array 
for i in range(N): 
    serial = input() #어떻게 비교할까 
    arr.append(serial) 



for i in range(N-1): 
    for j in range(i+1,N): 

        if len(arr[i])> len(arr[j]):     #조건1 : 
            arr[i],arr[j] = arr[j],arr[i]
        elif len(arr[i]) == len(arr[j]):
            suma=0
            sumb=0 
            for x,y in zip(arr[i],arr[j]):
                if x.isdigit():
                    suma+=int(x)
                if y.isdigit(): 
                    sumb+=int(y) 
            if suma>sumb: 
                arr[i],arr[j] = arr[j],arr[i] 
        
            elif suma == sumb: 
                for x,y in zip(arr[i],arr[j]):
                    if x>y: 
                     arr[i],arr[j]=arr[j],arr[i] 
                     break 
                    elif x<y:
                     break 


for i in arr: 
    print(i) 

'''

