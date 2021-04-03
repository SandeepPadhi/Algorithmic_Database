"""
Date:3/04/2021
667. Beautiful Arrangement II - Leetcode Medium

The following problme is solved using logic
"""


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        A=[i+1 for i in range(n)]
        for i in range(k+1):
            if i==0:
                A[i]=1
            elif i==1:
                A[i]=k+1
            elif i&1==0:
                A[i]=A[i-2]+1
            else:
                A[i]=A[i-2]-1
        for i in range(k+1,n):
            A[i]=i+1
        return A
        