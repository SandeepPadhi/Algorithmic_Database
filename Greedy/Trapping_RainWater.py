"""
Date:22/02/2021
42. Trapping Rain Water - Leetcode - Hard

The minheap solution is more intuitive then the DP solution and is also more general which 
                                            can be extended to 3D space.

The following program is solved using Min-heap.
At any point maxheight is the next greater height available starting from the ends.
So,all points that are less then current maxheight gets processed first .
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        Visited=[False]*len(height)
        heap=[]
        if 0<=len(height)<=2:
            return 0
        heapq.heappush(heap,(height[0],0))
        heapq.heappush(heap,(height[-1],len(height)-1))
        Visited[0],Visited[-1]=True,True
        maxheight=-1
        Water=0
        while(len(heap)):
            h,i=heapq.heappop(heap)
            maxheight=max(maxheight,h)
            for di in (-1,1):
                ni=i+di
                if 0<=ni<len(height) and not Visited[ni]:
                    heapq.heappush(heap,(height[ni],ni))
                    Visited[ni]=True
            #if h<maxheight:
            Water+=(maxheight-h)
        return Water

"""
Date:13/02/2021
The following program is solved using DP.
"""

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==0:
            return 0
        n=len(height)
        left=[0]*n
        right=[0]*n
        left[0]=height[0]
        for i in range(1,n):
            left[i]=max(height[i],left[i-1])
        
        right[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            right[i]=max(right[i+1],height[i])
        
        Water=0
        for i in range(n):
            Water+=(min(left[i],right[i])-height[i])
        return Water

"""