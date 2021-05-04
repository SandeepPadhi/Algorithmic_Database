"""
Date:4/05/2021
1655. Distribute Repeating Integers - Leetcode Hard

The following problem is solved using Bit masking + DP.

We use a technique of finding subset of bitmask...we find subset of 1's in the bitmask
i=mask
while(i>0):
    i=(i-1)^mask..where mask is the original mask..i is the subset mask generated
"""
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        Count=Counter(nums)
        Count=sorted([Count[c] for c in Count])
        #quantity.sort(reverse=True)
        M=len(Count)
        N=len(quantity)
        cache=[0]*(1<<N)
        
        for mask in range(1<<N):
            for j in range(N):
                if mask&(1<<j)>0:
                    cache[mask]+=quantity[j]
        
        @lru_cache(None)
        def find(index,mask):
            if mask==0:
                return True
            if index==M:
                return False
            
            i=mask
            while(i>0):
                total=cache[i]
                if total<=Count[index] and find(index+1,mask^i):
                    return True
                i=(i-1)&mask

            return find(index+1,mask)
        
        return find(0,(1<<N)-1)
            