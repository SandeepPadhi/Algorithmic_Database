"""
Date:29/04/2021
1223. Dice Roll Simulation - Leetcode Hard

DP solution- https://www.youtube.com/watch?v=6kaRxT7pI4I   ..by erricto go to 8 min


The following program is solved using DP+recursion
"""
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod=10**9 + 7
        dp=[[0 for _ in range(6)] for _ in range(n+1)]
        #initial
        for i in range(6):
            for l in range(1,min(n,rollMax[i])+1):
                dp[l][i]=1
        
        for i in range(1,n):
            for prev in range(6):
                for nxt in range(6):
                    if prev==nxt:
                        continue
                    for l in range(1,min(n,rollMax[nxt])+1):
                        if i+l>n:
                            break
                        dp[i+l][nxt]+=dp[i][prev]
                        dp[i+l][nxt]%=mod
        ans=0
        for a in range(6):
            ans+=dp[n][a]
            ans%=mod
        return ans
        
        
        
        
        """
        ans=0
        mod=10**9 + 7
        @lru_cache(None)
        def find(prev,count,ind):
            #nonlocal ans
            val=0
            if ind==n:
                return 1
            for i in range(6):
                if i==prev:
                    if count+1<=rollMax[i]:
                        val+=find(prev,count+1,ind+1)
                else:
                    val+=find(i,1,ind+1)
            return val%mod
                
        for i in range(6):
            ans+=find(i,1,1)
            ans%=mod
        
        return ans
        
        """