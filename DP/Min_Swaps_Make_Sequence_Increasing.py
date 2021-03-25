"""
Date:25/03/2021
801. Minimum Swaps To Make Sequences Increasing - Leetcode Medium

The following problem is solved using DP
"""
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        noswap=[len(A)]*len(A)
        swap=[len(A)]*len(A)
        noswap[0]=0
        swap[0]=1
        for i in range(1,len(A)):
            if A[i]>A[i-1] and B[i]>B[i-1] and A[i]>B[i-1] and B[i]>A[i-1]:
                noswap[i]=min(noswap[i-1],swap[i-1])
                swap[i]=min(noswap[i-1],swap[i-1])+1
            elif A[i]>A[i-1] and B[i]>B[i-1]:
                swap[i]=swap[i-1]+1
                noswap[i]=noswap[i-1]
            else:
                noswap[i]=swap[i-1]
                swap[i]=noswap[i-1]+1
        return min(swap[-1],noswap[-1])
                
        
        