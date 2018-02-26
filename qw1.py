t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    count=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i] | arr[j]) <= max(arr[i],arr[j]):
                count+=1
    print(count)
                
                
            
