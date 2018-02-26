t=int(input())
for i in range(t):
    n,h=map(int,input().split())
    ans=0
    count=0
    l1=[0]*n
    for j in range(n):
        l,h1=map(int,input().split())
        l=n-l-1
        h1=n-h1-1
        for k in range(h1,l+1):
            l1[k]+=1
    l1.sort()
    for g in range(len(l1)-1,-1,-1):
        ans+=n-l1[g]
        count+=1
        if count == h:
            break
    print(ans)
                
            
            
        
        
        
        
        
    
