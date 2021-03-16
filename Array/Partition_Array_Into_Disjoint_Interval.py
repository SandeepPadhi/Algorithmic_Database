"""
Date:16/03/2021
915. Partition Array into Disjoint Intervals - Leetcode Medium
The following program is solved using prefix-suffix arrays
"""

class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        
        N=len(A)
        G=[A[0]]*N
        L=[A[-1]]*N
        
        for i in range(1,N):
            G[i]=max(G[i-1],A[i])
        
        for i in range(N-2,-1,-1):
            L[i]=min(L[i+1],A[i])
        
        Par=N
        for i in range(N-1):
            if G[i]<=L[i+1]:
                Par=i+1
                break
        return Par