"""
Date:14/04/2021
1551. Minimum Operations to Make Array Equal - Leetcode Medium

The following problem is solved using Binary Search
"""
class Solution:
    def minOperations(self, n: int) -> int:
        A=[2*i + 1 for i in range(n)]
        low=0
        high=A[-1]
        ans=0
        while(low<=high):
            mid=(low+high)//2
            inc=0
            dec=0
            for a in A:
                if a<=mid:
                    inc+=abs(mid-a)
                if a>=mid:
                    dec+=abs(mid-a)
            
            if inc==dec:
                ans = inc
                high=mid-1
            elif inc>dec:
                high=mid-1
            else:
                low=mid+1
        return ans
                    
        