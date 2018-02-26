n=int(input())
x=list(map(int,input().split()))
y=[0]*n
p=0
x.sort()
for i in range(0,n,2):
    y[i]=x[p]
    p=p+1
for j in range(1,n,2):
    y[j]=x[p]
    p=p+1
for k in range(0,n):
    print(y[k],end=' ')
    
