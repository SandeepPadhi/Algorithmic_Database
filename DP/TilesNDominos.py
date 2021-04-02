"""
Date:2/04/2021
790. Domino and Tromino Tiling - Leetcode Medium

The following problem is solved using DP
"""
class Solution:
    def numTilings(self, N: int) -> int:
        if N==1:
            return 1
        M=10**9 + 7
        V=[0]*(N+1)
        H=[0]*(N+1)
        L=[0]*(N+1)
        V[0],V[1],V[2]=1,1,1
        H[0],H[1],H[2]=1,0,1
        L[0],L[1],L[2]=0,0,2
        for n in range(3,N+1):
            V[n]=V[n-1]+H[n-1]+L[n-1]
            H[n]=V[n-2]+H[n-2]
            L[n]=2*V[n-2]+2*H[n-2]+L[n-1]
        #print("V:{}".format(V))
        #print("H:{}".format(H))
        return (V[-1]+H[-1])%M
            
            