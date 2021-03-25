"""
Date:25/03/2021
1289. Minimum Falling Path Sum II - Leetcode Hard

The following problem is solved using DP
"""
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        import copy
        dp=copy.deepcopy(arr)
        for i in range(1,len(arr)):
            for j in range(len(arr[0])):
                d1=dp[i-1][:j]
                val=100000000
                if len(d1):
                    val=min(val,min(d1))
                d2=dp[i-1][j+1:]
                if len(d2):
                    val=min(val,min(d2))
                dp[i][j]+=val
        return min(dp[-1])
        