"""
Date:9/02/2021
923. 3Sum With Multiplicity - Leetcode Medium

The following problem is solved using hashing techique
"""
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count=0
        M=10**9 + 7
        for i in range(len(arr)):
            t=target-arr[i]
            lookup={}
            for j in range(len(arr)-1,i,-1):
                if t-arr[j] in lookup:
                    count+=lookup[t-arr[j]]
                if arr[j] not in lookup:
                    lookup[arr[j]]=0
                lookup[arr[j]]+=1
            count%=M
        return count
        