"""
Date:19/03/2021
78. Subsets - Leetcode Medium

The following problem is solved using bitwise tricks for generating all possible combinations
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        Result=[]
        for mask in range(2**len(nums)):
            Ans=[]
            i=0
            while(mask):
                if mask&1:
                    Ans.append(nums[i])
                i+=1
                mask>>=1
            
            Result.append(Ans)
        return Result
        