"""
Date:18/03/2021
1011. Capacity To Ship Packages Within D Days - Leetcode Medium

The following problem is solved using Binary Search
"""

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        #We will use binary search
        low=weights[0]
        high=sum(weights)
        maxweight=max(weights)
        minweight=min(weights)
        N=len(weights)
        
        
        def check(M):
            if M<maxweight:
                return False
            day=0
            s=0
            for i in range(N):
                s+=weights[i]
                if s>M:
                    day+=1
                    s=weights[i]
            day+=1
            if day>D:
                return False
            return True
        
        
        ans=high
        while(low<=high):
            mid=(low+high)//2
            if check(mid):
                ans = mid
                high = mid -1
            else:
                low = mid + 1
        return ans
            
            
            
        
        
        