t=int(input())
for i in range(0,t):
    str1=input().split()
    if len(str1) == 1:
        ans=str1[0][0].upper()
        for k in range (1,len(str1[0])):
            ans=ans+str1[0][k].lower()
        print(ans)
    else:
        ans=''
        for j in range(0,len(str1)-1):
            ans+=str1[j][0].upper()+'. '
        ans+=str1[len(str1)-1][0].upper()
        for k in range(1,len(str1[len(str1)-1])):
            ans+=str1[len(str1)-1][k].lower()
        print(ans)
                        
            
   
