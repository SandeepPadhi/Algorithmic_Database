"""
Date:11/03/2021
Coin Change
The following program is solved using DP
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        coins=[-1]+sorted(coins)
        dp=[[sys.maxsize]*(amount+1) for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0]=0
        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                if j-coins[i]>=0:
                    dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i]])
                else:
                    dp[i][j]=dp[i-1][j]
    
        return dp[-1][-1] if dp[-1][-1]!=sys.maxsize else -1
        