t=int(input())
for i in range(t):
    str1=input()
    str2=input()
    str3=''
    for j in range(len(str1)):
        if str1[j] == str2[j]:
            if str1[j] == 'W':
                str3+='B'
            else:
                str3+='W'
        else:
            str3+='B'
    print(str3)
                
