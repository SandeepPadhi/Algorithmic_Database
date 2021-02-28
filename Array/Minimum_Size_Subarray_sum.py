"""
Date:28/02/2021
209. Minimum Size Subarray Sum - Leetcode Medium

The following problem is solved using two-pointer technique
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        s=0 
        ans=len(nums)+1
        for right in range(len(nums)):
            s+=nums[right]
            if s>=target:
                #ans=min(ans,right-left+1)
                while(left<=right and s>=target):
                    ans=min(ans,right-left+1)
                    s-=nums[left]
                    left+=1
        return ans if ans<=len(nums) else 0