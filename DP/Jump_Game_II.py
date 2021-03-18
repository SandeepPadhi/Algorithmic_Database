"""
Date:18/03/2021
45. Jump Game II - Leetcode Medium

The following problem is solved using DP
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        MAX=1000
        N=len(nums)
        J=[MAX]*N
        J[0]=0
        for i in range(N-1):
            jump=nums[i]
            for j in range(1,jump+1):
                if i+j>=N:
                    break
                J[i+j]=min(J[i+j],1+J[i])
        return J[-1]