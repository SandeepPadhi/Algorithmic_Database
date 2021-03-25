"""
Date:23/03/2021
1143. Longest Common Subsequence - Leetcode Medium


The following problem is solved using DP
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
        #print("l:{} , w:{}".format(len(dp),len(dp[0])))
        for i in range(len(text2)):
            for j in range(len(text1)):
                #print("i:{},j:{}".format())
                if text2[i]==text1[j]:
                    dp[i+1][j+1]=1+dp[i][j]
                else:
                    dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
        return dp[-1][-1]
        