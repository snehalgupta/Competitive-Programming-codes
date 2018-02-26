
def range_prod(lo,hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        return range_prod(lo,mid) * range_prod(mid+1,hi)
    if lo == hi:
        return lo
    return lo*hi

def treefactorial(n):
    if n < 2:
        return 1
    return range_prod(1,n)

def puy(x):
 t=1
 res=1
 while x > 0: 
  t = t*x; 
  res = res+t 
  x =x- 1 
 return res 
 
def gcd(x, y):
 while y != 0:
  temp=x
  x=y
  y=temp%y
 return x
 
 
def euler(n, p, q):
 t = gcd(p, q)
 p=p//t
 q=q//t
 s=0
 z = 1
 while q > 0 and n > 0:
  t = p // q
  df=(z * t * n * (n + 1)) // 2
  s = s+df
  df=q * t
  p = p-df
  t = n // q
  df=z * p * t * (n + 1) - z * t * (p * q * t + p + q - 1) // 2
  s = s+df
  df=q * t
  n = n-df
  t = n * p // q
  df=z * t * n 
  s = s+df
  n = t 
  temp=p
  p=q
  q=temp
  z = -z 
 return s 
 
 
n = int(input())
print(euler(n, puy(3000), treefactorial(3000)))
