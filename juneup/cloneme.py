def main():
# User input
 t=int(input())
 for i in range(0,t):
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    
    sum1=[]
    sqr=[]
    six=[]
    s1=0
    s2=0
    s3=0
    
    for j in range(0,len(arr)):
        s1+=arr[j]
        s2+=arr[j]**2
        s3+=arr[j]**6
        sum1.append(s1) # cumulative sum of elements
        sqr.append(s2) # cumulative sum of square of elements
        six.append(s3) # cumulative sum of sixth power
        
    for k in range(0,q):
        a,b,c,d=map(int,input().split())
        # modifying indexes
        a-=1
        b-=1
        c-=1
        d-=1
        flagres=0
        #Calculating diff of sum of elements,squares and sixth power of elements in given range
        if a>0 :
            if c>0:
                cv1=-sum1[a-1]-(sum1[d]-sum1[c-1])+sum1[b]
                cv2=-sqr[a-1]-(sqr[d]-sqr[c-1])+sqr[b]
                cv3=-six[a-1]-(six[d]-six[c-1])+six[b]
            elif c==0:
                cv1=-sum1[a-1]-sum1[d]+sum1[b]
                cv2=-sqr[a-1]-sqr[d]+sqr[b]
                cv3=-six[a-1]-sqr[d]+six[b]
        elif a==0 :
            if c>0:
                cv1=-(sum1[d]-sum1[c-1])+sum1[b]
                cv2=-(sqr[d]-sqr[c-1])+sqr[b]
                cv3=-(six[d]-six[c-1])+six[b]
            elif c==0:
                cv1=-sum1[d]+sum1[b]
                cv2=-sum1[d]+sqr[b]
                cv3=-sum1[d]+six[b]
        # if b-a == 0 and (b-a)(b+a) == 0
        if cv1==0:
            if cv2==0 and abs(cv3)<0.01:
                flagres=0
            else:
                flagres=1
        else:
            if cv2%cv1 == 0:
                quo=cv2//cv1 
                x=(quo+cv1)//2 
                y=(quo-cv1)//2
                if (quo+cv1)%2 == 0 and (quo-cv1)%2==0:
                 if x>=1 and y>=1:
                    if abs(x**6-y**6-cv3)<0.01:
                        # Checking position of different elements
                        ta=0
                        taa=-1
                        tb=0
                        tbb=-1
                        
                        for vb in range(a,b+1):
                            if arr[vb]>x:
                                ta=ta+1
                            elif arr[vb]==x:
                                taa=taa+1
                            
                               
                        for vb1 in range(c,d+1):
                            if arr[vb1]>y:
                                tb=tb+1
                            elif arr[vb1]==y:
                                tbb=tbb+1
                            
                        if ta==tb:
                            flagres=0
                        else:
                            if ta+taa==tb or tb+tbb==ta:
                                flagres=0
                            else:
                                flagres=1
                    else:
                        flagres=1
                 else:
                     flagres=1
                else:
                    flagres=1
            else:
                flagres=1
        if flagres == 0:
         print("YES")
        else:
         print("NO")
main()                
