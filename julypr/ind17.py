mod = 1000000007
T = int(input())
for i in range(0,T):
    k = int(input())
    
    
    
    s= ((pow(2,k-1,mod)*(k*k-k+2)%mod-1+mod)%mod )
    print(s)
     
        
    
    
