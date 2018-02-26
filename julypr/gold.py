n=int(input())
arr=list(map(int,input().split()))
min1=arr[0]
sum1=0
l1=[]
for i in range(0,n):
    if arr[i] >= min1:
        l1.append(arr[i])
    else:
        ptr1=0
        ptr2=len(l1)-1
        while( ptr1<len(l1) and ptr2>= 0 and ptr1 < ptr2):
            sum1+=l1[ptr2]-l1[ptr1]
            ptr1+=1
            ptr2-=1
        l1=[arr[i]]
    min1=arr[i]
ptr1=0
ptr2=len(l1)-1
while( ptr1<len(l1) and ptr2>= 0 and ptr1 < ptr2):
    sum1+=l1[ptr2]-l1[ptr1]
    ptr1+=1
    ptr2-=1
l1=[]
print(sum1)
        
