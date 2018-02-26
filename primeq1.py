def sieve():
    global maxn
    global spf
    spf[1]=1
    for i in range(2,maxn):
        spf[i]=i
    for j in range(4,maxn,2):
        spf[j]=2
    for k in range(3,maxn):
        if k*k < maxn:
            if spf[k]==k:
                for l in range(k*k,maxn,k):
                    if spf[l]==l:
                        spf[l]=k
        else:
            break
def getfactors(x):
    global l1
    global l2
    curr=spf[x]
    cnt=1
    sum1=0
    while(x>1):
        x=x//spf[x]
        if(curr == spf[x]):
            cnt=cnt+1
            continue
        l1.append(curr)
        sum1+=cnt
        l2.append(sum1)
        curr=spf[x]
        cnt=1
def binarysearch(arr,x):
    l=0
    r=len(arr)-1
    if(arr[r] <= x):
        return len(arr)
    while l < r:
        m=(l+(r-l))//2
        if arr[m]<=x:
            l=m+1
        else:
            r=m
    return r     
 
n=int(input())
arr=list(map(int,input().split()))
maxn=1000001
spf=[0]*maxn
sieve()
factors=[]
exponents=[]

for w in arr:
    l1=[]
    l2=[]
    getfactors(w)
    factors.append(l1)
    exponents.append(l2)
    
 
q=int(input())
for i in range(0,q):
    l,r,x,y=map(int,input().split())
    result=0
    for cv in range(l-1,r):
           d1=0
           idx1=binarysearch(factors[cv],x-1)
           idx2=binarysearch(factors[cv],y)
           if idx1 == -1:
               idx1=len(factors[cv])
           if idx2 == -1:
               idx2 =len(factors[cv])
           if idx2 == 0:
               continue
           if idx1 > 0:
               d1=exponents[cv][idx1-1]
           if idx1 == idx2-1:
               result+=exponents[cv][idx1]
           else:
               result+=exponents[cv][idx2-1]-d1
               
    print(result)
