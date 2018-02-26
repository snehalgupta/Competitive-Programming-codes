def main():
    n,k=map(int,input().split())
    we=n//(2*(k+1))
    ans=n-((k+1)*we)
    print(we,end=' ')
    print(we*k,end=' ')
    print(ans)
main()
                
            
        
        
    
