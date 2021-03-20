"""
Date:19/03/2021
1046. Last Stone Weight - Leetcode Easy

The following problem is solved using Heap
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones =[-s for s in stones]
        heapq.heapify(stones)
        while(len(stones)>1):
            p1 = heapq.heappop(stones)
            p2= heapq.heappop(stones)
            p1,p2 = abs(p1),abs(p2)
            if p1>p2:
                heapq.heappush(stones,-(p1-p2))
    
    
        return -stones[0] if len(stones)==1 else 0
        
        
        