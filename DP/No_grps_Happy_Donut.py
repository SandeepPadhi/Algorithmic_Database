"""
Date:3/04/2021
1815. Maximum Number of Groups Getting Fresh Donuts - Leetcode Hard

The following program is solved using DP + logic
"""

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        n=len(groups)
        groups=[num%batchSize for num in groups if num%batchSize]
        ans=n-len(groups)
        
        freq=Counter(groups)
        for num in range(1,batchSize+1):
            matchnum=batchSize-num
            if num==matchnum:
                match=freq[num]//2
        
            else:
                match=min(freq[num],freq[matchnum])
            ans+=match
            freq[num]-=match
            freq[matchnum]-=match
        
        group=[]
        for f,c in freq.items():
            if c>0:
                group+=[f]*c
        
        @lru_cache(None)
        def dp(rem,group):
            if not group:
                return 0
            
            ans=0
            group=list(group)
            for i in range(len(group)):
                newgroup=group[:i] + group[i+1:]
                newrem=(rem+group[i])%batchSize
                ans=max(ans,dp(newrem,tuple(newgroup)))
        
            return (rem==0)  + ans
        
        
        return ans + dp(0,tuple(group))