#한수 
# 한수란 ? x의 각자리가 등차수열을 이룸 
# 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

'''
> 일, 십의자리는 다 만족 
> 백의자리만 판단하면 될듯 
> 10000 

'''
n = int(input()) 
cnt=n
if n//100 == 0: # 십의 자리 or 일의 자리
    print(n)
elif n==1000:
    print(144) 
else: 
    for i in range(n,0,-1): #뒤에서부터 돌면서 
        if i//100 ==0 : # 십의 자리 or 일의 자리까지 내려온다면 
           break
        else:
           a = i//100 # 백의자리 
           b = (i-(100*a)) // 10 # 십의자리 
           c = i-(100*a + 10*b) # 일의 자리 
           if (b-a)!=(c-b): # 등차수열이 아니면 
            cnt -=1 
    print(cnt)

# 정답은 맞췄으나 다른사람의 코드를 보고 현타가... 
# 리스트로 각자리를 구할수 있었던것을 
'''
# 1) 함수를 생성한 경우 
def hansu(num):
   hansu_cnt =0 
   for i in range(1,num+1):
      num_list=list(map(int,input().split(i)))
      if i<100: 
         hansu_cnt +=1 
      elif num_list[0]-num_list[1] == num_list[1] - num_list[2]:
         hansu_cnt +=1 

   return hansu_cntddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd


num=int(input())
print(hansu(num))


#2) 함수를 생성하지 않은 경우 
num=int(input())
hansu=0
for i in range(1,num+1):
   num_list = list(map(int,input().split(i)))
   if i<100:
      hansu+=1 
   elif num_list[0]-num_list[1] =d= num_list[1] - num_list[2]:
      hansu+=1 
      
print(hansu) 
'''

        