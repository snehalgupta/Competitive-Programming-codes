t=int(input())
for i in range(t):
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    res=0
    d1={}
    sum1=0
    s1=[]
    max1=0
    k=-1
    for j in range(n):
        sum1+=l2[j]
        s1.append(sum1)
        if d1.get(l1[j],-1) == -1:
            if k>=0:
                res=s1[j]-s1[k]
            else:
                res=s1[j]
            d1[l1[j]]=j
        else:
            if d1[l1[j]] > k:
                k=d1[l1[j]]
            res=s1[j]-s1[k]
            d1[l1[j]]=j
        if res>max1:
                max1=res
    print(max1)
            
            
            
