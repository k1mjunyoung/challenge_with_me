#베스트셀러 
#https://www.acmicpc.net/problem/1302

# 요소 개수 찾는 함수 
#input으로 주어진 list의 각요소가 해당 list에 몇번 나타나는지 수를 dictionart로 만들어서 리턴하기 

def get_element(my_list): 
    new_list={} 
    for i in my_list: 
        try: new_list[i] +=1 
        except:new_list[i]=1 

    return (new_list.values)


n = int(input())
my_list=[] 
for _ in range(n): 
    my_list.append(input()) 


print(get_element(my_list))




