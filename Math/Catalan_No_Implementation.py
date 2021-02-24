"""
Date:23/02/2021
The following program has many implementation of catalan numbers.
Link:https://www.geeksforgeeks.org/applications-of-catalan-numbers/
"""

N=7

#Implementation 1
dp=[False]*(N+1)
dp[0]=1
def catalan(N,dp):
    if dp[N]:
        return dp[N]
    Ans=0
    for i in range(N):
        Ans+=catalan(i,dp)*catalan((N-1)-i,dp)
    dp[N]=Ans
    return Ans
        
    
    
print(catalan(N,dp))
print(dp)

#Implementation - 2
fac=[False]*1000
fac[0],fac[1]=1,1
def factorial(N):
    if fac[N]:
        return fac[N]
    Ans=N*factorial(N-1)
    fac[N]=Ans
    return Ans

print(factorial(2*N)//((factorial(N)*factorial(N+1))))

#Implementation 3
def prodcatalan(N):
    import math
    if N==0 or N==1:
        return 1
    Ans=1
    for k in range(2,N+1):
        Ans*=((N+k)/k)
    return math.ceil(Ans)
print(prodcatalan(N))
    
    