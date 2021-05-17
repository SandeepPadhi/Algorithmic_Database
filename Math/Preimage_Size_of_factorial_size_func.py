"""
Date:17/05/2021
793. Preimage Size of Factorial Zeroes Function - Leetcode Hard

The following problem is solved using Binary search and by trick of counting no of 5's in fac(k) = (k//5) + (k//5*5) + (k/5*5*5)..so on
"""
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        
        def getzeros(val):
            
            start=5
            ans=0
            while((start<=val)):
                ans+=(val//start)
                start*=5
            return ans
        
        
        low=0
        high=(10**9)*5
        while(low<=high):
            mid=(low+high)//2
            ans=getzeros(mid)
            if ans==k:
                return 5
            elif ans<k:
                low=mid+1
            else:
                high=mid-1
        return 0
