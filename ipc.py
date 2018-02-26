t=int(input())
for i in range(0,t):
    n,d=map(int,input().split())
    sum1=0
    l1=[]
    for j in range(0,n):
        d1,t1,s1=map(int,input().split())
        x=d-d1+1
        if t1>x:
            y=t1-x
            t1=x
            for k in range(0,y):
                sum1+=s1
        for k1 in range(0,t1):
            l1.append(s1)
    l1.sort()
    for k2 in range(0,d):
        if len(l1)==0:
            break
        l1.pop()
    ans=sum1+sum(l1)
    print(ans)
        
        
        
