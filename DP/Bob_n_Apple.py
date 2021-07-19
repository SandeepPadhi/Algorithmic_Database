T=int(input())

for _ in range(T):
    N,M=map(int,input().split())
    P=[]
    V=[]
    for _ in range(N):
        v,p=map(int,input().split())
        P.append(p)
        V.append(v)
    
    half=0
    nothalf=1
    #Dp[items][maxprice][status]
    dp=[[[0,0] for _ in range(M+1)] for _ in range(N+1)]
    ans=0
    for item in range(1,N+1):
        for price in range(M+1):
            if False and item==0 and price==0:
                continue
            else:
                dp[item][price][nothalf]=dp[item-1][price][nothalf]
                dp[item][price][half]=max(dp[item-1][price][half],dp[item-1][price][nothalf])
                if P[item-1]<=price:
                    v1=V[item-1]+dp[item-1][price-P[item-1]][nothalf]
                    dp[item][price][nothalf]=max(dp[item][price][nothalf],v1)
                    
                    v2=V[item-1]+dp[item-1][price-P[item-1]][half]
                    dp[item][price][half]=max(dp[item][price][half],v2)
                    
                    v3=V[item-1]+dp[item-1][price-(P[item-1]//2)][nothalf]
                    dp[item][price][half]=max(v3,dp[item][price][half],dp[item][price][nothalf])
                    
                    ans=max(ans,dp[item][price][nothalf],dp[item][price][half])

                elif P[item-1]//2 <=price:
                    v3=V[item-1]+dp[item-1][price-(P[item-1]//2)][nothalf]
                    dp[item][price][half]=max(v3,dp[item][price][half],dp[item][price][nothalf])
                    ans=max(ans,dp[item][price][half])

    print(ans)
                    
                    
                    
                    
                    
                    
                    
                