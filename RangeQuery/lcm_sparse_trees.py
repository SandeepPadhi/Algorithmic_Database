"""
Date:28/01/2021
Following program is used to find lcm of Range:[L,R] using Sparse Table
"""
import math
S = [2, 8, 6, 9, 8, 6, 8, 2, 11,8,7] 
Lookup=[[1 for i in range(5)] for i in range(2*len(S))]

for i in range(len(S)):
    Lookup[i][0]=S[i]

j=1
n=len(S)

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def lcm(a,b):
    return (a*b)//gcd(a,b)

while((1<<j)<=n):
    i=0
    while(i+(1<<j)-1 < n):
        Lookup[i][j]=lcm(Lookup[i][j-1],Lookup[i+(1<<(j-1))][j-1])
        i+=1
    j+=1

def query(L,R):
    j=int(math.log2(R-L+1))
    return lcm(Lookup[L][j],Lookup[R-(1<<j)+1][j])


print(query(1,2))

