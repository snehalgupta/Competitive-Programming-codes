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
 
def func(x,y,z):
    return (x+y)*(y+z)
 
t=int(input())
for m in range(0,t):
    sum1=0
    p,q,r=map(int,input().split())
    p1=list(map(int,input().split()))
    q1=list(map(int,input().split()))
    r1=list(map(int,input().split()))
    p1.sort()
    q1.sort(reverse=True)
    r1.sort()
    for i in q1:
        index1=binarysearch(p1,i)
        index2=binarysearch(r1,i)
        if index1 == -1:
            index1=len(p1)
        if index2 == -1:
            index2=len(r1)
        if index1 > 0 and index2 > 0:
            sumx=sum(p1[0:index1])
            sumz=sum(r1[0:index2])
            sum1+=(i*index2*sumx)+(sumx*sumz)+(i*i*index1*index2)+(i*index1*sumz)
            p1=p1[0:index1]
            r1=r1[0:index2]
        else:
            break
    sum1=sum1%1000000007
    print(sum1)
                    
