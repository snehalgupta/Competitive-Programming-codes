def sieve():
    global factors
    maxn=1000001
    for i in range(2,maxn):
            if len(factors.get(i,[])) == 0:
                for j in range(2*i,maxn,i):
                    factors[j]=factors.get(j,[])+[i]
                factors[i]=[i]
factors={}
sieve()
for i in range(2,1000001):
    print(factors[i])
