"""
Date:19/03/2021
1331. Rank Transform of an Array - Leetcode Easy

The following program is solved using Hashing
"""
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        lookup={}
        for i in range(len(arr)):
            if arr[i] not in lookup:
                lookup[arr[i]]=[]
            lookup[arr[i]].append(i)
        A=sorted(list(set(arr)))
        Ans=[0]*len(arr)
        for i in range(len(A)):
            for ind in lookup[A[i]]:
                Ans[ind]=i+1
        return Ans
        
        
        