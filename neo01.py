t=int(input())
for i in range(0,t):
    l1=[]
    n,k=map(int,input().split())
    for lu in range(0,n):
        l5=set(map(int,input().split()[1:]))
        l1.append(l5)
    count=0
    for j in range(0,len(l1)):
        for b in range(j+1,len(l1)):
               
               l2=l1[j]|l1[b]
               
    
               if len(l2)==k:
                   count=count+1
                   
               
    print(count)
               
               
