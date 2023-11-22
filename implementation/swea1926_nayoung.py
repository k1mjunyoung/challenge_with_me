#간단한 369게임 
n = int(input())  # 입력 받기

tmp = []  # 결과를 저장할 리스트

for i in range(1, n+1):
    # 각 자리에 3, 6, 9가 있는지 확인
    count_of_369 = str(i).count('3') + str(i).count('6') + str(i).count('9')  # 문자열로 반환하는게 포인트 

    if count_of_369 > 0:
        tmp.append('-' * count_of_369)  # 3, 6, 9의 개수대로 '-'를 리스트에 추가
    else:
        tmp.append(str(i))  # 3, 6, 9가 없으면 i 그대로 리스트에 추가

# 리스트의 각 요소를 문자열로 이어붙여 출력
print(" ".join(tmp))


   
'''
1. n=int(input()) 입력받기 
2.for i in range(1,n+1) 
 2.1 i 각자리에 3이 있는지 확인 
 2.2 3이나 6이나 9가 이 있으면 3,6,9의 개수대로 '-'를 리스트에 넣어주기 
 2.3 없으면 i그대로 넣어주기 
3. print(" ".join(map(str,tmp))) 출력 



->  str(i)[0]은 숫자 i의 가장 왼쪽 자릿수에 해당하는 문자를 가져옵니다. 이런 식으로 각 자릿수에 접근할 수 있습니다.

'''
