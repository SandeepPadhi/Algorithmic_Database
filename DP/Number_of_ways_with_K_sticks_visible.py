"""
Date:24/05/2021
1866. Number of Ways to Rearrange Sticks With K Sticks Visible - Leetcode Hard

The following problem is solved using DP both recursion and tabulation
https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/discuss/1300169/VISULISATION-BY-IMAGE-or-Easy-Explanation

"""


from functools import lru_cache

mod=10**9 + 7

class Solution:

    @lru_cache(None)
    def rearrangeSticks(self, n: int, k: int) -> int:
        
        dp=[[0]*(k+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(k+1):                
                if i==j:
                    dp[i][j]=1
                elif j==0:
                    continue
                elif j>i:
                    continue
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]*(i-1)
                    dp[i][j]%=mod
        
        
        
        return dp[n][k]
        
        
        """
        
        @lru_cache(None)
        def go(n,k):
            if n==k:
                return 1
            if k>n:
                return 0
            if k==0:
                return 0

            return (go(n-1,k-1) + go(n-1,k)*(n-1))%mod
        return go(n,k)
        
        """