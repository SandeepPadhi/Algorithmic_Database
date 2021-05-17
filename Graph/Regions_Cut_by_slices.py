"""
Date:17/05/2021
959. Regions Cut By Slashes - Leetcode Medium

The following problem is solved using graphs..by converting given problem into graph of extended size beautifully.
This problem is a type of modification of number of Islands problem
"""
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        Row=len(grid)
        Col=len(grid[0])
        
        V= [[[False for _ in range(4)] for _ in range(Col) ] for _ in range(Row)]
        
        #print("{} ,{},{}".format(len(V),len(V[0]),len(V[0][0])))
        def dfs(row,col,piece):
            nonlocal V
            
            if row==Row or row<0 or col==Col or col<0 or V[row][col][piece]:
                #print("row:{},col:{}".format(row,col))
                return
            #print("yes")
            V[row][col][piece]=True
            
            
            if piece==0:
                dfs(row-1,col,2)
            if piece==1:
                dfs(row,col+1,3)
            if piece==2:
                dfs(row+1,col,0)
            if piece==3:
                dfs(row,col-1,1)
            
            if grid[row][col] !='/':
                
                #print("/ row:{},col:{}, piece:{} going to piece:{}".format(row,col,piece,piece^1))
                dfs(row,col,piece^1)
            if grid[row][col] !='\\':
                #print("\\ row:{} , col:{} ,piece:{} going to piece:{}".format(row,col,piece,piece^3))

                dfs(row,col,piece^3)
                
    
    
        no_of_regions=0
        for row in range(Row):
            for col in range(Col):
                for piece in range(4):
                    if not V[row][col][piece]:
                        dfs(row,col,piece)
                        no_of_regions+=1
        #print(V)
        return no_of_regions
                    