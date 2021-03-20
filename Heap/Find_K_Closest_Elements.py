"""
Date:19/03/2021
658. Find K Closest Elements

The following problem is solved using Heap
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        N=len(arr)
        for i in range(N):
            heapq.heappush(heap,(abs(arr[i] - x),arr[i]))
        
        Ans=[]
        for i in range(k):
            _,a = heapq.heappop(heap)
            Ans.append(a)
        return sorted(Ans)
        