def product(iterable):
    p=1
    for h in iterable:
        p=p*h
    return p
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
    

n,k = map(int, input().split())
y1=map(int,input().split())
y=list(y1)
count=0
y.sort()
b = product(y)
if b<=k:
    count=(1<<n)-1
else:

    for c in range(0,n):
        if y[c] <= k:
            count=count+1
        else:
            break
        
    for d in range(2,n+1):
        i=0
        j=d-2
        k1=0
        prod=product(y[0:j+1])
        cv=k/product(y[0:j+1])
        print("d "+str(d))
        while True:
            nmb = int(k/prod)
            ind = binarysearch(y[j+1:n],nmb)
            if ind != -1:
                count=count+ind
            else:
                count=count+len(y[j+1:n])
            print("j :"+str(j))
            print(count)
            if d == 2:
                prod=int(prod/y[j])*y[j+1]
                j=j+1
                if j == n-1:
                    break
            else:
                prod=int(prod/y[j])*y[j+1]
                print("product "+str(prod))
                j=j+1
                if(j == n-1):
                    k1=k1+1
                    if i+(d-1)*k1 == n-1:
                        k1=0
                        i=i+1
                        j=i+d-2
                        prod=product(y[i:j+1])
                    else:
                        j=i+(d-1)*k1
                        prod=product(y[i:j+1])/product(y[i+1:i+k1])
                if i == n-d+1 or y[i]>cv:
                    break
            
            
               
        


print(count)
