"""
Date:30/06/2021
368. Largest Divisible Subset - Leetcode Medium

The following problem is solved using DP and keeping tracking of parent
"""


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums=list(set(nums))
        nums.sort()
        N=len(nums)
        Parent=[i for i in range(N)]
        Size=[1 for _ in range(N)]
        ind=0
        maxsize=0
        for i in range(N):
            for j in range(i):
                if nums[i]%nums[j]==0 and Size[j]+1>Size[i]:
                    Size[i]=1+Size[j]
                    Parent[i]=j
                    if Size[i]>maxsize:
                        maxsize=Size[i]
                        ind=i
        
        Result=[]
        while(Parent[ind]!=ind):
            Result.append(nums[ind])
            ind=Parent[ind]
        
        
        Result.append(nums[ind])
        return Result