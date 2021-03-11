"""
Date:11/03/2021
1787. Make the XOR of All Segments Equal to Zero - Leetcode Hard

The following problem is solved using DP+observation
"""
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        freq=[Counter() for _ in range(k)]
        
        for i,num in enumerate(nums):
            freq[i%k][num]+=1
        
        totalcount=[ sum(f.values()) for f in freq]
        dp=[[sys.maxsize]*1024 for _ in range(k)]
    
        #Base Case
        for targetnum in range(1024):
            dp[-1][targetnum]=totalcount[-1]-freq[-1][targetnum]
        
        for i in range(k-2,-1,-1):
            changeall=totalcount[i]+min(dp[i+1])
            for xornum in range(1024):
                best=changeall
                for f in freq[i]:
                    best=min(best,totalcount[i]-freq[i][f]+dp[i+1][xornum^f])
                dp[i][xornum]=best
        return dp[0][0]
                    
                
                
                
        
        