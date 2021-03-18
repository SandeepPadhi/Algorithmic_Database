"""
Date18/03/2021
795. Number of Subarrays with Bounded Maximum - Leetcode Medium

The following problem is solved using dp

"""
class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        res,dp=0,0
        prev=-1
        
        for i in range(len(A)):
            if A[i]<L:
                res+=dp
            if A[i]>R:
                prev=i
                dp=0
            if L<=A[i]<=R:
                res+=(i-prev)
                dp=i-prev
                
        return res