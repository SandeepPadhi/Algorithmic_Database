"""
Date:17/02/2021
1673. Find the Most Competitive Subsequence - Leetcode Medium

The following program is solved using Stack.
"""

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        #Longest Increasing rrrr
        S=collections.deque()
        for i in range(len(nums)):
            while(S and S[-1]>nums[i] and len(S)-1+len(nums)-i>=k):
                S.pop()
            if len(S)<k:
                S.append(nums[i])
        return list(S)
        
                