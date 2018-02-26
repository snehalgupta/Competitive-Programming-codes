def nextgreater(arr,n):
    global ng
    stack=[]
    for i in range(n-1,-1,-1):
        while len(stack)!= 0:
            if arr[stack[len(stack)-1]] <= arr[i]:
                stack.pop()
            else:
                break
        if len(stack) != 0:
            ng[i]=stack[len(stack)-1]
        else:
            ng[i]=-1
        stack.append(i)

def nextsmaller(arr,n):
    global ns
    stack=[]
    for i in range(n-1,-1,-1):
        while len(stack)!= 0:
            if arr[stack[len(stack)-1]] >= arr[i]:
                stack.pop()
            else:
                break
        if len(stack) != 0:
            ns[i]=stack[len(stack)-1]
        else:
            ns[i]=-1
        stack.append(i)
    
n=int(input())
l1=list(map(int,input().split()))
ng=[0]*n
ns=[0]*n

nextgreater(l1,n)
nextsmaller(l1,n)
sum1=0
for j in range(0,n):
    if ng[j] == -1:
        sum1=sum1+15
    elif ns[ng[j]] == -1:
        sum1=sum1+10
    else:
        sum1=sum1+5
print(sum1)


