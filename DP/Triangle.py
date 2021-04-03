"""
Date:3/04/2021
120. Triangle - Leetcode Medium

The following problem is solved using DP
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        T=[]
        for i in range(1,len(triangle)):
            #print("T:{}".format(T))
            for j in range(len(triangle[i])):
                
                if j==0:
                    triangle[i][j]+=triangle[i-1][j]
                elif j==len(triangle[i])-1:
                    triangle[i][j]+=triangle[i-1][j-1]
                else:
                    triangle[i][j]+=min(triangle[i-1][j-1],triangle[i-1][j])
        #print(triangle)
        return min(triangle[-1])
        