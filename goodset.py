t=int(input())
l1=[1,2]
sum1=[3]
sum2=3
i=3
while i<501:
    if i not in sum1:
        l1.append(i)
        for k in range(0,len(l1)-1):
            sum1.append(i+l1[k])
    i=i+1
for d in range(0,t):
    n=int(input())
    
    for g in range(0,n):
        print(l1[g],end=" ")
    print()

        
    
    
