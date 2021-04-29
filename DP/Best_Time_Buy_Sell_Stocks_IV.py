"""
Date:29/04/2021
188. Best Time to Buy and Sell Stock IV - Leetcode Hard

The following problem is solved using DP
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        if k==0:
            return 0
        MIN=-100000000000000
        N=len(prices)
        K=2*k
        if K>=N:
            ans=0
            for i in range(N-1):
                if prices[i]<prices[i+1]:
                    ans+=prices[i+1]-prices[i]
            return ans
        
        
        dp=[[MIN]*(K+1) for _ in range(N+1)]
        dp[0][0]=0
        dp[1][1]=-prices[0]
        for i in range(2,N+1):
            dp[i][1]=max(dp[i-1][1],-prices[i-1])
        ans=0
        for k in range(2,K+1):

            for i in range(1,N+1):
                if k&1:
                        dp[i][k]=dp[i-1][k-1]-prices[i-1]
                else:
                        dp[i][k]=dp[i-1][k-1]+prices[i-1]
                dp[i][k]=max(dp[i][k],dp[i-1][k])
                        #print(dp)
                ans=max(ans,dp[i][k])
        #print(dp)
        return ans
        