import math
t=int(input())
for i in range(0,t):
    n,b=map(int,input().split())
    if b>=n:
        print(0)
    else:
        ans=n//b
        t1=math.ceil(ans/2)
        ans1=t1*(n-(t1*b))
        print(ans1)
            
            
            
