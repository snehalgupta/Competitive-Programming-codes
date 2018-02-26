def count(n,k,l, m):
    
    if k < 1:
        raise StopIteration
    if k == 1:
        if n <= m and n>=l :
            yield (n,)
        raise StopIteration
    for i in range(l,m+1):
        for result in count(n-i,k-1,i,m):                
            yield result+(i,)

def findceil(arr,first,l,h):
    ceilindex=l
    for j in range (l,h):
        if arr[j] > first and arr[j] < arr[ceilindex]:
            ceilindex=j
    return ceilindex

def permute(arr):
    global count1
    size=len(arr)
    arr.sort()
    isfinished = False
    while(isfinished == False):
        count1=count1+1
        i=size-2
        
        while arr[i] >= arr[i+1]:
            i=i-1
        if i == -1:
            isfinished=True
        else:
            ceilindex=findceil(arr,arr[i],i+1,size)
            temp=arr[i]
            arr[i]=arr[ceilindex]
            arr[ceilindex]=temp
            arr[i+1:].sort()
    
    

t=int(input())
for i in range (1,t+1):
    count1=0
    n,k,m=map(int,input().split())
    if n % k == 0 :
                g = int(n / k)
                flag=0
    else :
                g = int(n / k) + 1
                flag=1            
    x=list(count(n,g,1,k))
    if flag == 0 :
        print(str(g)+" "+str(1))
    else:
        for j in x:
            permute(list(j))
        print(str(g)+" "+str(count1))
    
    
    
    
    
                    
                    
                
