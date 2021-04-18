"""
Date:18/04/2021
1590. Make Sum Divisible by P - Leetcode Medium

The following problem is solved using Hash map
"""
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total=sum(nums)
        remainder=total%p
        if remainder==0:
            return 0
        lookup={0:-1}
        Prefix=[0]
        ans=1000000000000
        for i,num in enumerate(nums):
            Prefix.append(Prefix[-1]+num)
            r=(Prefix[-1] - remainder)%p
            if r in lookup:
                ans=min(ans,i-lookup[r])
            lookup[Prefix[-1]%p]=i
        
        if ans<len(nums):
            return ans
        return -1
                