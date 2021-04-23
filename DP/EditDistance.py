"""
Date:23/04/2021
72. Edit Distance - Leetcode Hard

The following problem is solved using DP
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp=[[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]
        for i in range(len(dp[0])):
            dp[0][i]=i
        for j in range(len(dp)):
            dp[j][0]=j
        #i=word1 , j=word2
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                if word2[i-1]==word1[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1 + min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
        return dp[-1][-1]
        
        
        """
        
        @lru_cache(None)
        def dp(i,j):
            if i==0:
                return j
            if j==0:
                return i
            if word1[i-1]==word2[j-1]:
                return dp(i-1,j-1)
            
            return 1 + min(dp(i,j-1),dp(i-1,j-1),dp(i-1,j))
        return dp(len(word1),len(word2))
        
        """