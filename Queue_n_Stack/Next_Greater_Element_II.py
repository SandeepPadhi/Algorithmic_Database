"""
Date:25/02/2021
503. Next Greater Element II - Leetcode Medium  

The following program is solved using monotonic stack
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nextgreater=[-1]*len(nums)
        stack=[]
        for i in range(len(nums)):
            while(len(stack) and nums[stack[-1]]<nums[i]):
                p=stack.pop()
                nextgreater[p]=nums[i]
            stack.append(i)
        while(len(stack)):
            p=stack.pop()
            for i in range(len(nums)):
                if nums[i]>nums[p]:
                    nextgreater[p]=nums[i]
                    break
        return nextgreater