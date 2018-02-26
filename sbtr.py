n,m = map(int,input().split())
l = list(map(int,input().split()))
for i in range(m):
    a,b = map(int,input().split())
if(n == m+1):
    print(0)
else:
    print(n)
    for i in range(0,n):
        print(i+1,end=' ')
    print()
 
