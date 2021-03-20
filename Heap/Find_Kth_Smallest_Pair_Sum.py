"""
Date:19/03/2021
373. Find K Pairs with Smallest Sums - Leetcode Medium

The following program is solved using Heap
"""

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap=[]
        i=0
        for n1 in nums1:
            for n2 in nums2:
                heapq.heappush(heap,(n1+n2,i,(n1,n2)))
                i+=1
        Ans=[]
        while(k>0 and len(heap)>0):
            _,_,p = heapq.heappop(heap)
            Ans.append(p)
            k-=1
        return Ans
        