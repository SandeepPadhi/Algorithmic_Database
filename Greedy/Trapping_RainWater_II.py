"""
Date:22/02/2021

407. Trapping Rain Water II - Leetcode Hard

The following problem is solved using min-heap of heights.
We first store heights of the boundaries.Then,we store all subsequent heights moviing inward from outside to inside.

Everytime,we take the next bigger height.
"""

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        row=len(heightMap)
        col=len(heightMap[0])
        Visited=[[False for _ in range(col)] for _ in range(row)]
        heap=[]
        for i in range(row):
            for j in range(col):
                if i==0 or j==0 or i==row-1 or j==col-1:
                    heapq.heappush(heap,(heightMap[i][j],i,j))
                    Visited[i][j]=True
        
        Water=0
        maxheight=-1
        while(len(heap)):
            h,i,j=heapq.heappop(heap)
            maxheight=max(maxheight,h)
            for di,dj in ((-1,0),(0,-1),(1,0),(0,1)):
                ni,nj=i+di,j+dj
                if 0<=ni<row and 0<=nj<col and not Visited[ni][nj]:
                    heapq.heappush(heap,(heightMap[ni][nj],ni,nj))
                    Visited[ni][nj]=True
                    
            
            Water+=(maxheight-h)
        return Water
            
                    

    
    
    
    



"""
Date:14/02/2021
The idea of 1D trapping RainWater does not work for 2D trapping Rain_water
The following program is solved using DP,But it is not the correct Ans.
"""
"""
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        row=len(heightMap)
        col=len(heightMap[0])
        
        left=[[heightMap[i][j] for j in range(col)] for i in range(row)]
        right=[[heightMap[i][j] for j in range(col)] for i in range(row)]
        up=[[heightMap[i][j] for j in range(col)] for i in range(row)]
        down=[[heightMap[i][j] for j in range(col)] for i in range(row)]
        #for left
        for j in range(1,col):
            for i in range(row):
                left[i][j]=max(left[i][j],left[i][j-1])
        
        #for right
        for j in range(col-2,-1,-1):
                    for i in range(row):
                        right[i][j]=max(right[i][j],right[i][j+1])
        
        #for Up
        for i in range(1,row):
            for j in range(col):
                up[i][j]=max(up[i][j],up[i-1][j])
        
        #for Down
        for i in range(row-2,-1,-1):
            for j in range(col):
                down[i][j]=max(down[i][j],down[i+1][j])
        
        Trapwater=0
        for i in range(1,row-1):
            for j in range(1,col-1):
                Trapwater=Trapwater+(min(left[i][j],right[i][j],up[i][j],down[i][j]) - heightMap[i][j])
        return Trapwater



[[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
    
    
    
    

"""