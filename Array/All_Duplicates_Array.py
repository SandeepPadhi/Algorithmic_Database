"""
Date:18/03/2021

442. Find All Duplicates in an Array


The following program is solved using Arrays and position trick
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        Ans=[]
        for i in range(len(nums)):
            k=abs(nums[i]) - 1
            if nums[k]<0:    
                Ans.append(abs(nums[i]))
            nums[k]=-nums[k]
        return Ans
        
       