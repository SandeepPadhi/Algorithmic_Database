"""
Date:6/04/2021
887. Super Egg Drop


The following problem is solved using DP - We find number of floors we can test with m moves and k eggs

dp[m][e]=dp[m-1][e-1](if egg breaks) +  dp[m-1][e](if egg doesnt break) + 1
"""
class Solution:
    
    def superEggDrop(self, k: int, n: int) -> int:
        
        dp=[[0 for _ in range(k+2)] for _ in range(n+2)]
        for m in range(1,n+1):
            for e in range(1,k+1):
                dp[m][e]=1+dp[m-1][e-1]+dp[m-1][e]
                if dp[m][e]>=n:
                    return m

    """
    Date:6/04/2021
    887.Super Egg Drop - leetcode Hard

    The following problem is solved using recursion and dp ---> Gives TLe
    """

        
        
    """
    @lru_cache(None)
    def superEggDrop(self, k: int, n: int) -> int:
        if k==1:
            return n
        if n==0 or n==1:
            return n
        minmove=1000000000
        for f in range(1,n+1):
            res=max(self.superEggDrop(k-1,f-1),self.superEggDrop(k,n-f))
            if res<minmove:
                minmove=res
        return minmove+1
    
    """