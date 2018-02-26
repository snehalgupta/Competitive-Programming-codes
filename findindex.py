

import bisect
 
def main():
    n=int(input())
    arr=input().split()
    l1=[]
    d1={}
    for i in range(0,len(arr)):
        count1=0
        for j in arr[i]:
            if j=='0':
                l1.append(i)
                count1=count1+1
            d1[i]=count1
            
    q=int(input())
    for f in range(q):
        str1=list(map(int,input().split()))
        if str1[0] == 1:
            if str1[1] > len(l1):
                 print("-1")
            else:
                print(l1[str1[1]-1])
        elif str1[0] == 0:
            count=0
            for t in str(str1[2]):
                if t == '0':
                    count=count+1
            diff=count-d1.get(str1[1],0)
            if diff>0:
                for cv in range(diff):
                    bisect.insort(l1,str1[1])
            elif diff<0:
                index=bisect.bisect_left(l1,str1[1])
                del l1[index:index+abs(diff)]
                    
            d1[str1[1]]=d1.get(str1[1],0)+diff
main()
            
                    
                
            

