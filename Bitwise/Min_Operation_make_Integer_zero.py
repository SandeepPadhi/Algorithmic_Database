"""
Date:4/05/2021
1611. Minimum One Bit Operations to Make Integers Zero - Leetcode Hard

The following problem is solved using bit manipulation and observation
here,count=stores previous values
ans=stores current ans
"""
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        count=0
        ans=0
        for i in range(32):
            if n&(1<<i):
                #print("yes")
                ans=(1<<(i+1))-1-count
                count=ans
        
        
        return ans