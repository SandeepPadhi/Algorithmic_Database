"""
Date:25/02/2021

496. Next Greater Element I - Leetcode Easy

The following program is solved using Monotone Stack.
Idea behind is elements in the stack at subjected to some change due to newly arrived elements.
The results of the change are stored in separate answer
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextgreater=[-1]*(max(nums2)+1)
        stack=[]
        for i in range(len(nums2)):
            while(len(stack) and nums2[stack[-1]]<nums2[i]):
                p=stack.pop()
                nextgreater[nums2[p]]=nums2[i]
            stack.append(i)
        Result=[]
        for n in nums1:
            Result.append(nextgreater[n])
        return Result