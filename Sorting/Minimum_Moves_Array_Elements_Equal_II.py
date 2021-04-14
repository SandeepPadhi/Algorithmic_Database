"""
Date:14/04/2021
462. Minimum Moves to Equal Array Elements II - Leetcode Medium

The following program is solved by sorting and logic

The idea is that minimum distance is obtained by always choosing the median element in sorted array
"""
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        #print(nums)
        count=0
        mid=len(nums)//2
        for n in nums:
            count+=abs(n-nums[mid])
        return count
        