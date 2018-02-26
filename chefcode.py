import itertools
def binarysearch(arr,x):
    l=0
    r=len(arr)-1
    if(arr[r] <= x):
        return -1
    while l < r:
        m=int(l+(r-l)/2)
        if arr[m]<=x:
            l=m+1
        else:
            r=m
    return r
 
def product(iterable):
    p=1
    for h in iterable:
        p=p*h
    return p
 
 
n,k = map(int, input().split())
y1=map(int,input().split())
y=list(y1)
count=0
y.sort()
 
n=len(y)
for i in range(1,n+1):
    count1=0
    temp = int( k / product(y[0:i-1]))
    index1=binarysearch(y,temp)
    if index1 != -1:
        index=index1
    else:
        index=n
        
    
    if index != -1:
        for subset in itertools.combinations(y[0:index],i):
            ans=product(subset)

            if(ans <= k):
                count1=count1+1
                count=count+1
    
    
                
print(count)
