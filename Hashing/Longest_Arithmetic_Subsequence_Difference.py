"""
Date:25/03/2021
1218. Longest Arithmetic Subsequence of Given Difference - Leetcode Medium

The following problem is solved using Hashing
"""

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        Umap={}
        N=len(arr)
        U=[1]*N
        d=difference
        for i in range(N):
            Best=0
            a=arr[i]
            if a-d in Umap:
                Best=Umap[a-d]
            
            U[i]=Best+1
            Umap[a]=Best+1
        
        return max(U)
            
        