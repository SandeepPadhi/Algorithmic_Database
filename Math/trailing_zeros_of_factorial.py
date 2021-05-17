

"""
Date:17/05/2021
172. Factorial Trailing Zeroes - Leetcode Easy

The trick is counting no of 5's in fac(k) = (k//5) + (k//5*5) + (k/5*5*5)..so on

"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans=0
        x=5
        while(x<=n):
            ans+=(n//x)
            x*=5
        return ans
        