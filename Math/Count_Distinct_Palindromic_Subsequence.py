"""
Date:5/04/2021
730. Count Different Palindromic Subsequences

Here,we count subsequences having a*a,b*b,c*c,d*d types

The following problem is solved using DP+recursion
"""
class Solution(object):
    def countPalindromicSubsequences(self, S):
        lookup={}
        M=10**9 + 7
        def dfs(S):
            nonlocal lookup
            if S not in lookup:
                count=0
                for s in set(S):
                    start=S.find(s)
                    end=S.rfind(s)
                    if start==-1:
                        continue
                    count+= 1 if start==end else 2+dfs(S[start+1:end])
                lookup[S]=count%M
            return lookup[S]
        
        
        
        return dfs(S)%M