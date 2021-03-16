"""
Date:16/03/2021
1486. XOR Operation in an Array - Leetcode Easy

The following problem is solved using simple iteration
"""
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans=0
        for i in range(n):
            ans^=(start + 2*i)
        return ans