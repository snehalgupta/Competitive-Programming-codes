t=int(input())
for i in range(t):
    a,b,n=map(int,input().split())
    if n%2==0:
        if a>b:
            print(a//b)
        else:
            print(b//a)
    else:
        a=a*2
        if b>a:
            print(b//a)
        else:
            print(a//b)

