"""
Date:30/06/2021
1524. Number of Sub-arrays With Odd Sum - Leetcode Medium

The following problem is solved using counting odd and even values
"""
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod=10**9 + 7
        even=1
        odd=0
        ans=0
        S=0
        for a in arr:
            S+=a
            if S&1:
                ans+=even
                odd+=1
            else:
                ans+=odd
                even+=1
            
        
        
        return ans%mod