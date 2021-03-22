"""
Date:20/03/2021
329. Longest Increasing Path in a Matrix - Leetcode Hard

The following problem is solved using DP
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        Path=[[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        Best = 0    
            
        def find(i,j):
            nonlocal Path
            if Path[i][j]!=-1:
                return Path[i][j]
            N=[]
            M=0
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni,nj=i+di,j+dj
                if ni>=0 and ni<len(matrix) and nj>=0 and nj<len(matrix[0]) and matrix[ni][nj]>matrix[i][j] :
                    M=max(M,find(ni,nj))
            Path[i][j]=M+1
            return M+1
            
                
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                find(i,j)
                Best=max(Best,Path[i][j])
        
        return Best