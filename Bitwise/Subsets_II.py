"""
Date:18/03/2021
90. Subsets II - Leetcode Medium

The following program is solved using Bitwise trick to generate all possible combinations
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        Result=set()
        for mask in range(2**len(nums)):
            Ans=[]
            i=0
            while(mask):
                if mask&1:
                    Ans.append(nums[i])
                i+=1
                mask>>=1
            Result.add(tuple(Ans))
        return list(Result)
        
        