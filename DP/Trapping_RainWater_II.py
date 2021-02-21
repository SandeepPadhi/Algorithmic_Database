"""
Date:13/02/2021
Leetcode-Hard
The following program is solved using DP.
It is an extension of Trapping Rainwater problem leetcode.
"""
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        row=len(heightMap)
        col=len(heightMap[0])
        
        left=[[heightMap[i][j] for j in range(col)] for i in range(row)]
        right=[[heightMap[i][j] for j in range(col)] for i in range(row)]
        up=[[heightMap[i][j] for j in range(col)] for i in range(row)]
        left=[[heightMap[i][j] for j in range(col)] for i in range(row)]
        #for left
        for j in range(1,col)
            for i in range(row):
                left[i][j]=max(left[i][j],left[i][j-1])
        
        #for right
        for j in range(col-2,-1,-1)
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
        for i in range(row):
            for j in range(col):
                Trapwater+=(min(left[i][j],right[i][j],up[i][j],down[i][j]) - heightMap[i][j])
        return Trapwater



