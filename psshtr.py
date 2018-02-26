def binarySearch(arr, l, r, x):
 
    while l <= r:
 
        mid = l + (r - l)//2;
         
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
 
        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
 
        # If x is smaller, ignore right half
        else:
            r = mid - 1
     
    # If we reach here, then the element was not present
    return -1

def binarysearch(arr,x):
    l=0
    r=len(arr)-1
    if(arr[r] <= x):
        return len(arr)
    while l < r:
        m=l+(r-l)//2
        if arr[m]<=x:
            l=m+1
        else:
            r=m
    return r

def dfs1(curr,prev,val):
    global map1
    global cnt
    global queries
    global qk
    global values
    global qu
    global qv
    global qa
    global adj
    global cost
    global qb
    if curr != 0:
        pos=map1[val]
        update(1,0,cnt-1,pos,val)
    for i in range(len(queries[curr])):
        nex=queries[curr][i]
        k=qk[nex]
        ans=0
        if(len(values) != 0):
            index=binarySearch(values,0,len(values)-1,k)
            if index<0:
                index=binarysearch(values,k)
                pos=index-1
            else:
                pos=index
            
            if pos>= 0:
                ans=find(1,0,cnt-1,0,pos)
        if qu[nex] == curr:
            qa[nex]=ans
        if qv[nex] == curr:
            qb[nex]=ans
    for i1 in range(len(adj[curr])):
        nex=adj[curr][i1]
        if nex != prev:
            dfs1(nex,curr,cost[curr][i1])
    if curr != 0:
        pos=map1[val]
        update(1,0,cnt-1,pos,val)

def find(index,l,r,x,y):
    global st
    if l>= x and r<= y:
        return st[index]
    mid=(l+r)//2
    if y <= mid:
        return find(index*2,l,mid,x,y)
    elif x>mid:
        return find(index*2+1,mid+1,r,x,y)
    else:
        return find(index*2,l,mid,x,mid)^find(index*2+1,mid+1,r,mid+1,y)
def update(index,l,r,pos,val):
    global st
    if l==r:
        st[index]^=val
        return
    mid=(l+r)//2
    if pos<= mid:
        update(index*2,l,mid,pos,val)
    else:
        update(index*2+1,mid+1,r,pos,val)
    st[index]=st[index*2]^st[index*2+1]

            
            
                
                
            
        
t=int(input())
for i1 in range(t):
    n=int(input())
    adj=[]
    cost=[]
    map1=dict()
    queries=[]
    values=[]
    for hy in range(n):
        queries.append([])
        adj.append([])
        cost.append([])
    for i in range(1,n):
        u,v,c=map(int,input().split())
        u=u-1
        v=v-1
        adj[u].append(v)
        cost[u].append(c)
        adj[v].append(u)
        cost[v].append(c)
        if(map1.get(c,-1) == -1):
            map1[c]=0
            values.append(c)

    cnt=len(map1)
    values.sort()
    for i2 in range(len(map1)):
        map1[values[i2]]=i2
    m=int(input())
    qu=[0]*m
    qv=[0]*m
    qk=[0]*m
    qa=[0]*m
    qb=[0]*m
    
    
    
    for i3 in range(m):
        l2=list(map(int,input().split()))
        qu[i3]=l2[0]-1
        qv[i3]=l2[1]-1
        qk[i3]=l2[2]
        queries[qu[i3]].append(i3)
        queries[qv[i3]].append(i3)
        
    st=[0]*(4*cnt)
    dfs1(0,-1,0)
    for iy in range(m):
        ans=qa[iy]^qb[iy]
        print(ans)
    
        
        
        
        
