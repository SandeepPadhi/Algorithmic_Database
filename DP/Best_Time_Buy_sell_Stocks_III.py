"""
Date:29/04/2021
123. Best Time to Buy and Sell Stock III - Leetcode Hard

The following problem is solved using DP
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N=len(prices)
        K=4
        if K>=N:
            ans=0
            for i in range(N-1):
                if prices[i]<prices[i+1]:
                    ans+=(prices[i+1]-prices[i])
            return ans
        
        
        Min=-10000000
        dp=[[0]*(K+1) for _ in range(N+1)]
        for i in range(K+1):
            dp[0][i]=Min
        dp[0][0]=0
        
        ans=0
        for k in range(1,K+1):
            for i in range(1,N+1):

                if k&1:
                    dp[i][k]=dp[i-1][k-1]-prices[i-1]
                else:
                    dp[i][k]=dp[i-1][k-1]+prices[i-1]
            
                
                dp[i][k]=max(dp[i][k],dp[i-1][k])
                ans=max(ans,dp[i][k])
        return ans