"""
Date:3/04/2021
775. Global and Local Inversions - Leetcode Medium

The following problem is solved using logic
"""

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        maxval=-1
        for i in range(len(A)-2):
            maxval=max(maxval,A[i])
            if maxval>A[i+2]:
                return False
        return True
                    