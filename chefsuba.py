from collections import deque
 
n,k,p=map(int,(input().split()))
 
 
maxs=deque()
stack=deque()
 
y1=map(int,input().split())
x=input()
j=0
y=deque(y1)
 
 
if(n <= k):
            
            max_sum=sum(y)
            while(j < p):
                if x[j] == '?':
                    print(max_sum)
                j=j+1
            
            
            
else :
            sum1=0
            
            for th in range(0,k):
                sum1+=y[th]
            
            first_sum=sum1
            window_sum=sum1
            stack.append(sum1)
            maxs.append(sum1)
            for l in range (k,n):
                  window_sum+=y[l]-y[l-k]
                  stack.append(window_sum)
                  xz = maxs.pop()
                  maxs.append(xz)
                  if window_sum >= xz :
                      maxs.append(window_sum)
                  
            
            
                
 
 
            while j < p :
    
    
                if x[j] == '!':
        
                          y.rotate(1)
                          
                          s=first_sum-y[k]+y[0]
                          first_sum=s
                          stack.appendleft(s)
                          lkj=stack.pop()
                          jhg=maxs.pop()
                          if lkj != jhg :
                              maxs.append(jhg)
                          zqw=maxs.pop()
                          maxs.append(zqw)
                          if ( s > zqw):
                
                                maxs=deque([s])
                          elif s == zqw:
                              flag=0
                              while(flag == 0):
                                  if maxs[0] < s:
                                      maxs.popleft()
                                      
                                  else:
                                      flag=1
                                      break
                              maxs.appendleft(s)
            
                          else:
                                if s > maxs[0]:
                                    bnp=0
                                    while bnp == 0:
                                        if maxs[0] < s:
                                            maxs.popleft()
                                            
                                        else:
                                            bnp=1
                                            break
                                
                                maxs.appendleft(s)
                          
            
                else:
                    max_sum=maxs.pop()
                    maxs.append(max_sum)
                    print(max_sum)
                    while( j+1 < p):
                
                     if(x[j+1] == '?'):
                    
                        print(max_sum)
                        j=j+1
                    
                     else:
                        break
            
            
    
 
                j=j+1
