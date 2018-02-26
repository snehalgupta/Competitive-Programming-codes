def binarysearch(arr,x,r):
    l=0
    
    if(arr[r] <= x):
        return -1
    while l < r:
        m=int(l+(r-l)/2)
        if arr[m]<=x:
            l=m+1
        else:
            r=m
    return r
 
def func(x,y,z):
    return (x+y)*(y+z)
 
t=int(input())
for m in range(0,t):
    sum1=0
    p,q,r=map(int,input().split())
    p1=list(map(int,input().split()))
    q1=list(map(int,input().split()))
    r1=list(map(int,input().split()))
    p1.sort()
    q1.sort(reverse=True)
    r1.sort()
    if q1[q-1] >= p1[p-1] and q1[q-1] >= r1[r-1] :
        
        ts=0
        for g in q1:
            ts+=g*g
        s1=sum(p1)
        s2=sum(q1)
        s3=sum(r1)
        sum1=(s2*r*s1)+(s1*s3*q)+(ts*p*r)+(s2*p*s3)
    elif q1[0] < p1[0] or q1[0]<r1[0] :
        
        sum1=0
    elif q1[q-1] >= p1[p-1] and q1[q-1] < r1[r-1] :
        bn=0
        sr=[]
        sumx=sum(p1)
        o1=len(r1)-1
        for i in q1:
            index2=binarysearch(r1,i,o1)
            if bn == 0:
                su=0
                for v in range(0,index2):
                    su=su+r1[v]
                    sr.append(su)
                bn=bn+1
                    
            if index2== -1:
                index2=o1+1
            if index2>0:
                o1=index2-1
                sumz=sr[index2-1]
                sum1+=(i*index2*sumx)+(sumx*sumz)+(i*i*p*index2)+(i*p*sumz)
            else:
                break
    elif q1[q-1] >= r1[r-1] and q1[q-1]<p1[p-1]:
        bn=0
        sr=[]
        sumz=sum(r1)
        o1=len(p1)-1
        for i in q1:
            index1=binarysearch(p1,i,o1)
            if bn == 0:
                su=0
                for v in range(0,index1):
                    su=su+p1[v]
                    sr.append(su)
                bn=bn+1
            if index1== -1:
                index1=o1+1
            if index1>0:
                o1=index1-1
                sumx=sr[index1-1]
                sum1+=(i*r*sumx)+(sumx*sumz)+(i*i*index1*r)+(i*index1*sumz)
            else:
                break
    else:
        bn=0
        sr1=[]
        sr2=[]
        o1=len(p1)-1
        o2=len(r1)-1
        for i in q1:
            index1=binarysearch(p1,i,o1)
            index2=binarysearch(r1,i,o2)
            
            if index1 == -1:
                index1=o1+1
            if index2 == -1:
                index2=o2+1
            if bn ==0 :
                su1=0
                su2=0
                for v1 in range(0,index1):
                    su1=su1+p1[v1]
                    sr1.append(su1)
                for v2 in range(0,index2):
                    su2=su2+r1[v2]
                    sr2.append(su2)
                bn=bn+1
            if index1 > 0 and index2 > 0:
                o1=index1-1
                o2=index2-1
                sumx=sr1[index1-1]
                sumz=sr2[index2-1]
                sum1+=(i*index2*sumx)+(sumx*sumz)+(i*i*index1*index2)+(i*index1*sumz)
                
            else:
                break
    sum1=sum1%1000000007
    print(sum1)
 
