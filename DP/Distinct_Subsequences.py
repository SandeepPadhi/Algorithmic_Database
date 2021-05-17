"""
Date:9/05/2021
115. Distinct Subsequences - Leetcode Hard

The following program is solved using DP
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(t)
        m=len(s)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(m+1):
            dp[0][i]=1
        
        for i in range(n):
            for j in range(m):
                dp[i+1][j+1]=dp[i+1][j]
                if t[i]==s[j]:
                    dp[i+1][j+1]+=dp[i][j]
        return dp[-1][-1]