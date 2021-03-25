"""
Date:25/03/2021
174. Dungeon Game - Leetcode Hard

The following program is solved using DP.
Depending the path,decides whether ones has to do the bottom-up or top-down
"""

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n=len(dungeon),len(dungeon[0])
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                #print("i:{},j:{}".format(i,j))
                if i==m-1 and j==n-1:
                    dungeon[i][j]=min(dungeon[i][j],0)*-1 + 1
                elif i==m-1:
                    dungeon[i][j]= max(dungeon[i][j+1]-dungeon[i][j],1)
                elif j==n-1:
                    dungeon[i][j]= max(dungeon[i+1][j]-dungeon[i][j],1)
                else:
                    dungeon[i][j] =  max(min(dungeon[i+1][j],dungeon[i][j+1])-dungeon[i][j],1)
        
        
        return dungeon[0][0]