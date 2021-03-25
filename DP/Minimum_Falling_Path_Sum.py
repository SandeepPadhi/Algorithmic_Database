"""
Date:25/03/2021
931. Minimum Falling Path Sum - Leetcode Medium

The followng problem is solved using DP
"""
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        import copy
        dp=copy.deepcopy(matrix)
        m=len(matrix)
        n=len(matrix[0])
        for i in range(1,m):
            for j in range(n):
                minval=10000000
                for di,dj in [(-1,0),(-1,-1),(-1,+1)]:
                    ni,nj=i+di,j+dj
                    if 0<=ni<m and 0<=nj<n:
                        minval=min(minval,dp[ni][nj])
                #print("i:{} , j:{} , minval:{}".format(i,j,minval))
                dp[i][j]+=minval
        #print("dp:{}".format(dp))
        #print("matrix:{}".format(matrix))
        return min(dp[-1])
                    
                        
                