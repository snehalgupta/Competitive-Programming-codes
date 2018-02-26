t=int(input())
for i in range(0,t):
    l1=input().split()
    l2=input().split()
    d1={}
    count=0
    flag=0
    for i in l1:
        d1[i]=1
    for j in l2:
        if d1.get(j,0) == 1:
            count=count+1
            d1[j]+=1
            if count == 2:
                flag=1
                break
    if flag==1:
        print("similar")
    else:
        print("dissimilar")
                
            
