"""
Date:24/02/2021
1155. Number of Dice Rolls With Target Sum - Leetcode - Medium

Very Important

The following program is solved using DP
"""
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        Ans=0
        M=10**9+7
        
        dp=[[0]*(target+1) for _ in range(d+1)]
        for i in range(d+1):
            dp[i][i]=1
        dp[0][0]=1
        for d1 in range(1,d+1):
            for t in range(d1+1,target+1):
                way=0
                for f1 in range(1,f+1):
                    if t-f1>=0:
                        way+=dp[d1-1][t-f1]
                    else:
                        break

                dp[d1][t]=way%M
        return dp[-1][-1]