"""
Date:19/03/2021
719. Find K-th Smallest Pair Distance  - Leetcode Hard

The following problem is solved using Binary Search
"""
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = 0
        high = nums[-1]
        ans=-1
        
        while(low<=high):
            mid = (low + high)//2
            count =0
            left=0
            right =0
            
            while(right<len(nums)):
                while(nums[right]-nums[left]>mid):
                    left+=1
                count+=(right-left)
                right+=1
            
            if count>=k:
                ans = mid
                high = mid -1
            else:
                low = mid + 1
        
        
        
        return ans
        
        