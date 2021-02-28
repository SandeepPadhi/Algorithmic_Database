"""
Date:28/02/2021
1775. Equal Sum Arrays With Minimum Number of Operations -Leetcode Medium

The following program is solved using greedy approach.
Idea:Greater side has to decrease and smaller side has to increase

"""

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        total1=sum(nums1)
        total2=sum(nums2)
        if total1==total2:
            return 0
        if total1<total2:
            nums=[6-num for num in nums1]+[num-1 for num in nums2]
        else:
            nums=[num-1 for num in nums1]+[6-num for num in nums2]
        nums.sort(reverse=True)
        d=abs(total1-total2)
        ans=0
        for i in range(len(nums)):
            d-=nums[i]
            ans+=1
            if d<=0:
                return ans
        return -1