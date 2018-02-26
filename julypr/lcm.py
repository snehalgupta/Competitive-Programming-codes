def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
def lcm(x,y):
    return (x*y)//gcd(x,y)
n=int(input())
a,b,c=map(int,input().split())
sum1=0
sum1+=(n//a)+(n//b)+(n//c)
lcm1=lcm(a,b)
lcm2=lcm(b,c)
lcm3=lcm(a,c)
sum1-=(n//lcm1)+(n//lcm2)+(n//lcm3)
sum1+=n//lcm(a,lcm2)
print(sum1)
                            
