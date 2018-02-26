def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

def inverse(a,m):
    m0=m
    x0=0
    x1=1
    if m == 1:
        return 0
    while a>1:
        q=a//m
        t=m
        m=a%m
        a=t
        t=x0
        x0=x1-q*x0
        x1=t
    if x1<0:
        x1+=m0
    return x1
    
    

def main():
    t=int(input())
    for i in range(t):
        n=int(input())
        n=n-1
        if n==0:
            print("0 0")
        else:
            num=(n+1)*n
            den=2*(2*n-1)
            gc=gcd(num,den)
            num=num//gc
            den=den//gc
            m1=1000000007
            m2=1000000009
            ans1=(num*inverse(den,m1))%m1
            ans2=(num*inverse(den,m2))%m2
            print(str(ans1)+" "+str(ans2))
main()
        
        
            
        
