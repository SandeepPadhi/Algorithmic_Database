"""
Date:12/02/2021
VERY IMPORTANT
1547. Minimum Cost to Cut a Stick - Leetcode Hard

The following program is solved using DP.
"""
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts=[0]+cuts+[n]
        cuts.sort()
        dp=[[0 for _ in range(100+2)] for _ in range(100+2)]

        for size in range(2,len(cuts)):
            for i in range(len(cuts)-size):
                j=i+size
                dp[i][j]=1000000000
                for k in range(i+1,j):
                    dp[i][j]=min(dp[i][j],cuts[j]-cuts[i]+dp[i][k]+dp[k][j])
        return dp[0][len(cuts)-1]



