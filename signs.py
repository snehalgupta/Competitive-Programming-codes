t=int(input())
for i in range(0,t):
    s=input()
    prev=s[0]
    count=1
    max1=1
    for j in range(0,len(s)):
        if s[j] == '<' or s[j] == '>':
            if s[j] == prev or prev == '=':
                count+=1
            else:
                count=1
                count+=1
            if count>max1:
                max1=count
            prev=s[j]
    print(max1)
                
                
        
            
        
