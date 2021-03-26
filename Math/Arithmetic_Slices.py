"""
Date:26/03/2021
413. Arithmetic Slices - Leetcode Medium

The following problem is solved using Maths
"""
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        start=0
        end=2
        N=len(nums)
        Ans=0
        while(end<N):
            if nums[end]-nums[end-1]==nums[end-1]-nums[end-2]:
                end+=1
            else:
                l=end-start
                if l>=3:
                    l=l-2
                    val = l*(l+1)//2
                    Ans+=val
                start=end-1
                end=end+1
        l=end-start
        if l>=3:
            l=l-2
            val= l*(l+1)//2
            Ans+=val
        return Ans
        
        