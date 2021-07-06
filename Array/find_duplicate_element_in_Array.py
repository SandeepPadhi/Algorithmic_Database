"""
Date:30/06/2021
287. Find the Duplicate Number - Leetcode Medium

The following program is solved using logic
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        N=len(nums)
        for i in range(N):
            ind=abs(nums[i])
            if nums[ind]<0:
                return ind
            nums[ind]=-nums[ind]

            
            
