"""
Date:30/06/2021
1584. Min Cost to Connect All Points - Leetcode Medium

The following program is solved using Prim's Algorithm
"""

INF=100000000
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N=len(points)
        MST=[False]*N
        Key=[INF]*N
        ans=0
        heap=[(0,0)]
        i=0
        while(i<N):
            key,point1=heapq.heappop(heap)
            if MST[point1]:
                continue
            #print("point:{},key:{}".format(point1,key))
            MST[point1]=True
            ans+=key
            x1,y1=points[point1]
            for point2 in range(N):
                if point1!=point2 and not MST[point2]:
                    x2,y2=points[point2]
                    dis=abs(x1-x2)+abs(y1-y2)
                    heapq.heappush(heap,(dis,point2))
            i+=1
        #print("i:{}".format(i))
        return ans
                    
            
            