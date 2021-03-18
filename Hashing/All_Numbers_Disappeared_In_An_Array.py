"""
Date:18/03/2021
448. Find All Numbers Disappeared in an Array

The following problem is solved using hashing
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        Ans = set(i for i in range(1,len(nums)+1))
        for n in nums:
            Ans.discard(n)
        return list(Ans)
        