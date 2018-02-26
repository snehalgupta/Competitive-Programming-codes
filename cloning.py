
from heapq import heappush, heappop, heapify 
 
class MinHeap:
     
    def __init__(self):
        self.heap = [] 
 
    def parent(self, i):
        return (i-1)/2
     
    def insert(self, k):
        heappush(self.heap, k)
        
def binarysearch(arr,x):
    l=0
    r=len(arr)-1
    if(arr[r] <= x):
        return -1
    while l < r:
        m=l+(r-l)//2
        if arr[m]<=x:
            l=m+1
        else:
            r=m
    return r
def first(arr, low, high, x):

    if(high >= low):
        mid = low + (high - low)//2
        if( ( mid == 0 or x > arr[mid-1]) and arr[mid] == x):
            return mid
        elif(x > arr[mid]):
            return first(arr, (mid + 1), high, x)
        else:
            return first(arr, low, (mid -1), x)
    
    return -1

def last( arr, low,  high,  x):

    if (high >= low):
    
        mid = low + (high - low)//2
        if (( mid == len(arr)-1 or x < arr[mid+1]) and arr[mid] == x):
            return mid
        elif (x < arr[mid]):
            return last(arr, low, (mid -1), x)
        else:
            return last(arr, (mid + 1), high, x)
    
    return -1

    
t=int(input())
for i in range(0,t):

    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    for j in range(0,q):
        a,b,c,d=map(int,input().split())
        leng=b-a+1
        d1={}
        d2={}
        heapobj = MinHeap()
        for k in range(0,leng):
            heapobj.insert(arr[k+c-1])
            d1[arr[k+a-1]]=d1.get(arr[k+a-1],0)+1
            d2[arr[k+c-1]]=d2.get(arr[k+c-1],0)+1
    l1=heapobj.heap
    kj=[]
    vj=[]
    for k1 in d1.keys():
        cv=d1[k1]-d2.get(k1,0)
        if d2.get(k1,0) != 0:
            del d2[k1]
        if cv != 0:
            kj.append(k1)
            vj.append(cv)
    if len(kj)==0:
        
        print("YES")
    elif len(vj)==1:
        
        if vj[0]==1:
            idx=binarysearch(l1,kj[0])
            if idx==-1:
                idx=len(l1)-1
            for t in d2.keys():
                we=t
            if l1[idx]==we:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    elif len(vj)==2:
        
        if vj[0]==1 and vj[1]==-1:
            if kj[0]>kj[1]:
                idx=first(l1,0,len(l1)-1,kj[0])
                if idx == -1:
                    idx=binarysearch(l1,kj[0])
                    if idx == -1:
                        idx=len(l1)-1
                    if l1[idx]==kj[1]:
                        print("YES")
                    else:
                        print("NO")
                else:
                    if l1[idx-1] == kj[1]:
                        print("YES")
                    else:
                        print("NO")
            else:
                idx=last(l1,0,len(l1)-1,kj[0])
                if idx == -1:
                    idx=binarysearch(l1,kj[0])
                    if idx == -1:
                        idx=len(l1)-1
                    if l1[idx] == kj[1]:
                        print("YES")
                    else:
                        print("NO")
                else:
                    if l1[idx+1] == kj[1]:
                        print("YES")
                    else:
                        print("NO")
        elif vj[0]==-1 and vj[1]==1:
            if kj[1]>kj[0]:
                idx=first(l1,0,len(l1)-1,kj[1])
                if idx == -1:
                    idx=binarysearch(l1,kj[1])
                    if idx == -1:
                        idx=len(l1)-1
                    if l1[idx] == kj[0]:
                        print("YES")
                    else:
                        print("NO")
                else:
                    if l1[idx-1] == kj[0]:
                        print("YES")
                    else:
                        print("NO")
            else:
                idx=last(l1,0,len(l1)-1,kj[1])
                if idx == -1:
                    idx=binarysearch(l1,kj[1])
                    if idx == -1:
                        idx=len(l1)-1
                    if l1[idx] == kj[0]:
                        print("YES")
                    else:
                        print("NO")
                else:
                    if l1[idx+1] == kj[0]:
                        print("YES")
                    else:
                        print("NO")
            
        else:
            print("NO")
    else:
        
        print("NO")
            
        
            
            
        
        
        
        
            
        
            
            
