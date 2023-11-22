for test_case in range(1,11): 
    N=int(input()) 
    total=0
# tmp=[]
    buildings = list(map(int,input().split()))
    for i in range(2,len(buildings)-2): 
        if (buildings[i-1]<buildings[i]) and (buildings[i]>buildings[i+1]):
          if (buildings[i-2]<buildings[i]) and (buildings[i]>buildings[i+2]):
             tmp = max(buildings[i-2],buildings[i-1],buildings[i+1],buildings[i+2]) 
             cnt = abs(buildings[i]-tmp)
             total+=cnt
 
 
    print("#{} {}".format(test_case,total))