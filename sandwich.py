import itertools
def count ( a,b,c,d ):
    if b < 1 :
        raise StopIteration
    if b == 1 :
        if a<=d and a>=c :
            yield (a,)
        raise StopIteration
    for j in range(c,d+1):
        for x in count(a-j,b-1,j,d):
            yield x+(j,)
            
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                
                yield perm[:i] + elements[0:1] + perm[i:]

   
t=int(input())
for i in range (1,t+1):
            lookup = [[[0]*125000]*125000]*125000
            n,k,m=map(int,input().split())
            if n % k == 0 :
                g = int(n / k)
                flag=0
            else :
                g = int(n / k) + 1
                flag=1
            count1=0
            li=list(count(n,g,1,k))
            print(li)
            for subset in li :
                ki=list(all_perms(subset))
                count1+=len(ki)
            if(flag == 0 ):
                print(str(g)+" "+str(1))
            else:
                print(str(g)+" "+str((count1)%m))



        
