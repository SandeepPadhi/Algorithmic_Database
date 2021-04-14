"""
Date:12/04/2021
327. Count of Range Sum - Leetcode Hard

The following problem is solved using Hashing
"""
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        hashmap=defaultdict(lambda:0)
        prefix=[0]
        cnt=0
        hashmap[0]=1
        for n in nums:
            prefix.append(prefix[-1]+n)
            for target in range(lower,upper+1):
                cnt+=hashmap[prefix[-1]-target]
            hashmap[prefix[-1]]+=1
                
        
        return cnt
        
        
                    