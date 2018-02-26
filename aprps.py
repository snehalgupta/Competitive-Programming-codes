import math
def calc(arr,m):
    n=len(arr)
    coeff=[0]*(n+1)
    coeff[0]=-arr[0]
    coeff[1]=1
    for k in range(2,n+1):
        coeff[k]=1
        for i in range(k-2,-1,-1):
            coeff[i+1]=coeff[i]-(arr[k-1]*coeff[i+1])
        coeff[0]=-arr[k-1]*coeff[0]
    result=coeff[n-m]
    if (n-m)%2 != 0:
        result=-result
    return result
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x
t=int(input())
for i in range(t):
    n=int(input())
    m=1000000007
    l1=list(map(int,input().split()))
    if n == 1:
        print(2)
        for e in range(n):
            l1[e]=isqrt(l1[e])
        l2=[]
        l2.append(l1[0])
        l2.append(-l1[0])
        l3=[]
        for i in range(0,3):
            sum1=calc(l2,i)
            print(sum1)
            l3.append(sum1%m)
        while(len(l3) != 0):
            print(str(l3.pop()),end=' ')
            
        
    elif n==2:
        print(4)
        ans1=abs(l1[0]-l1[1])
        ans1=(ans1*ans1)%m
        ans2=((-2)*(l1[0]+l1[1]))%m
        print(str(ans1)+" 0 "+str(ans2)+" 0 1")
        print(4)
        
            
        l2=[]
        l2.append((l1[0]+l1[1]))
        l2.append((l1[0]-l1[1]))
        l2.append((-l1[0]+l1[1]))
        l2.append((-l1[0]-l1[1]))
        l3=[]
        for i in range(0,5,2):
            sum1=calc(l2,i)
            if sum1<0:
                l3.append(int(-math.sqrt(abs(sum1)))%m)
            else:
                l3.append(math.sqrt(sum1)%m)
            
            
        while(len(l3) != 1):
            print(str(l3.pop()),end=' 0 ')
        print(l3[0])

       
        
        
    elif n==3:
        print(8)
        
        l2=[1]
        l3=[1]
        l4=[1]
        prod2=1
        prod3=1
        prod4=1
        for k in range(4):
                        prod2=prod2*l1[0]
                        l2.append(prod2)
                        prod3=prod3*l1[1]
                        l3.append(prod3)
                        prod4=prod4*l1[2]
                        l4.append(prod4)
        a1=(l2[4]+l3[4]+l4[4])
        a2=-4*(l2[3]*(l1[1]+l1[2])+l3[3]*(l1[0]+l1[2])+l4[3]*(l1[0]+l1[1]))
        a3=6*(l2[2]*l3[2]+l3[2]*l4[2]+l2[2]*l4[2])
        a4=4*(l2[2]*l1[1]*l1[2]+l3[2]*l1[0]*l1[2]+l4[2]*l1[0]*l1[1])
        ans1=(a1+a2+a3+a4)%m
        ans2=(6*(l2[2]+l3[2]+l4[2])+4*(l1[0]*l1[1]+l1[1]*l1[2]+l1[0]*l1[2]))%m
        ans3=(-4*(l1[0]+l1[1]+l1[2]))%m
        ans4=(-4*(l2[3]+l3[3]+l4[3])+4*(l2[2]*(l1[1]+l1[2])+l3[2]*(l1[0]+l1[2])+l4[2]*(l1[0]+l1[1]))+(-40)*l1[0]*l1[1]*l1[2])%m
        print(str(ans1)+" 0 "+str(ans4)+" 0 "+str(ans2)+" 0 "+str(ans3)+" 0 1")
    elif n == 4:
        print(16)
        for e in range(n):
            l1[e]=isqrt(l1[e])
        l2=[]
        l2.append(l1[0]+l1[1]+l1[2]+l1[3])
        l2.append(l1[0]+l1[1]-l1[2]+l1[3])
        l2.append(l1[0]+l1[1]+l1[2]-l1[3])
        l2.append(l1[0]+l1[1]-l1[2]-l1[3])
        l2.append(l1[0]-l1[1]+l1[2]+l1[3])
        l2.append(l1[0]-l1[1]-l1[2]+l1[3])
        l2.append(l1[0]-l1[1]+l1[2]-l1[3])
        l2.append(l1[0]-l1[1]-l1[2]-l1[3])
        l2.append(-l1[0]+l1[1]+l1[2]+l1[3])
        l2.append(-l1[0]+l1[1]-l1[2]+l1[3])
        l2.append(-l1[0]+l1[1]+l1[2]-l1[3])
        l2.append(-l1[0]+l1[1]-l1[2]-l1[3])
        l2.append(-l1[0]-l1[1]+l1[2]+l1[3])
        l2.append(-l1[0]-l1[1]-l1[2]+l1[3])
        l2.append(-l1[0]-l1[1]+l1[2]-l1[3])
        l2.append(-l1[0]-l1[1]-l1[2]-l1[3])
        l3=[]
        for i in range(0,17):
    
            sum1=calc(l2,i)
            l3.append(sum1%m)
        while(len(l3) != 0):
            print(str(l3.pop()),end=' ')
        
    elif n==5:
        for e in range(n):
            l1[e]=isqrt(l1[e])
        print(32)
        l2=[]
        l2.append(l1[0]+l1[1]+l1[2]+l1[3]+l1[4])
        l2.append(l1[0]+l1[1]+l1[2]-l1[3]+l1[4])
        l2.append(l1[0]+l1[1]+l1[2]+l1[3]-l1[4])
        l2.append(l1[0]+l1[1]+l1[2]-l1[3]-l1[4])
        l2.append(l1[0]+l1[1]-l1[2]+l1[3]+l1[4])
        l2.append(l1[0]+l1[1]-l1[2]-l1[3]+l1[4])
        l2.append(l1[0]+l1[1]-l1[2]+l1[3]-l1[4])
        l2.append(l1[0]+l1[1]-l1[2]-l1[3]-l1[4])
        l2.append(l1[0]-l1[1]+l1[2]+l1[3]+l1[4])
        l2.append(l1[0]-l1[1]+l1[2]-l1[3]+l1[4])
        l2.append(l1[0]-l1[1]+l1[2]+l1[3]-l1[4])
        l2.append(l1[0]-l1[1]+l1[2]-l1[3]-l1[4])
        l2.append(l1[0]-l1[1]-l1[2]+l1[3]+l1[4])
        l2.append(l1[0]-l1[1]-l1[2]-l1[3]+l1[4])
        l2.append(l1[0]-l1[1]-l1[2]+l1[3]-l1[4])
        l2.append(l1[0]-l1[1]-l1[2]-l1[3]-l1[4])
        l2.append(-l1[0]+l1[1]+l1[2]+l1[3]+l1[4])
        l2.append(-l1[0]+l1[1]+l1[2]-l1[3]+l1[4])
        l2.append(-l1[0]+l1[1]+l1[2]+l1[3]-l1[4])
        l2.append(-l1[0]+l1[1]+l1[2]-l1[3]-l1[4])
        l2.append(-l1[0]+l1[1]-l1[2]+l1[3]+l1[4])
        l2.append(-l1[0]+l1[1]-l1[2]-l1[3]+l1[4])
        l2.append(-l1[0]+l1[1]-l1[2]+l1[3]-l1[4])
        l2.append(-l1[0]+l1[1]-l1[2]-l1[3]-l1[4])
        l2.append(-l1[0]-l1[1]+l1[2]+l1[3]+l1[4])
        l2.append(-l1[0]-l1[1]+l1[2]-l1[3]+l1[4])
        l2.append(-l1[0]-l1[1]+l1[2]+l1[3]-l1[4])
        l2.append(-l1[0]-l1[1]+l1[2]-l1[3]-l1[4])
        l2.append(-l1[0]-l1[1]-l1[2]+l1[3]+l1[4])
        l2.append(-l1[0]-l1[1]-l1[2]-l1[3]+l1[4])
        l2.append(-l1[0]-l1[1]-l1[2]+l1[3]-l1[4])
        l2.append(-l1[0]-l1[1]-l1[2]-l1[3]-l1[4])
        l3=[]
        
        for i in range(0,33):
            sum1=calc(l2,i)
            l3.append(sum1%m)
            
            
        while(len(l3) != 0):
            print(str(l3.pop()),end=' ')
        
        
       
        
    
            
    
            
            
    
        
