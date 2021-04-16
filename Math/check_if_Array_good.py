"""
Date:15/04/2021
1250. Check If It Is a Good Array - Leetcode Hard

The following problem is solved using bezout's theorem
"""
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        g=0
        for n in nums:
            g=gcd(g,n)
        return g==1
        
        