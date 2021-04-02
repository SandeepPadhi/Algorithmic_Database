"""
Date:3/03/2021
330. Patching Array - Leetcode Hard

The following problem is solved using simple loop
"""
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch=0
        count=0
        N=n
        for n in nums:
            while count<N and count+1<n:
                patch+=1
                count+=(count+1)
            if count>=N:
                break
            count+=n
        while(count<N):
            patch+=1
            count+=(count+1)
        return patch   