t=int(input())
for i in range(t):
    s=input()
    u=[]
    d=[]
    for j in range(1,len(s)):
        if s[j] != s[j-1]:
            if s[j] == 'U':
                d.append(1)
            elif s[j]=='D':
                u.append(1)
    if s[len(s)-1]=='U':
        u.append(1)
    elif s[len(s)-1]=='D':
        d.append(1)
    if len(u)== 0 or len(d)==0 :
        print(0)
    elif len(u) < len(d):
        print(len(u))
    else:
        print(len(d))
            
