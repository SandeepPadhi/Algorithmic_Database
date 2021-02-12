"""
Date:10/02/2021
Following program is solved using Dynamic programming.
It is solved using bottom up approach.
O(N^3) time complexity
"""
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        dp=[[[-1 for _ in range(col)] for _ in range(col)] for _ in range(row)]
        dp[0][0][-1]=grid[0][0]+grid[0][-1]
        maxval=dp[0][0][-1]
        for i in range(1,row):
            for c1 in range(col):
                for c2 in range(col):
                    val=0
                    if c1==c2:
                        val=grid[i][c1]
                    else:
                        val=grid[i][c1]+grid[i][c2]

                    colval=-1
                    c1col=[-1,0,1]
                    c2col=[-1,0,1]
                    for dc1 in c1col:
                        for dc2 in c2col:
                            col1,col2=c1+dc1,c2+dc2
                            if col1<0 or col1>=col or col2<0 or col2>=col:
                                continue
                            if dp[i-1][col1][col2]!=-1:
                                                                
                                colval=max(colval,val+dp[i-1][col1][col2])
                    dp[i][c1][c2]=colval
                    maxval=max(maxval,dp[i][c1][c2])
        return maxval

    
    
    
    
    
    """
    def cherryPickup(self, grid: List[List[int]]) -> int:
        import numpy as np
        board=[[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
        row=len(grid)
        col=len(grid[0])
        for i in range(row-2,-1,-1):
            for j in range(col):
                if j==0:
                    board[i][j]=max(board[i+1][j],board[i+1][j+1])
                elif j==col-1:
                    board[i][j]=max(board[i+1][j],board[i+1][j-1])
                else:
                    board[i][j]=max(board[i+1][j],board[i+1][j-1],board[i+1][j+1])
                board[i][j]+=grid[i][j]
        print(np.array(board))
        
        r1=0
        r2=col-1
        cherry=grid[0][0]+grid[0][-1]
        for i in range(row-1):
            r1val=[]
            r2val=[]
            if r1==0:
                r1val=[(board[i+1][0],0),(board[i+1][1],1)]
            elif r1==col-1:
                r1val=[(board[i+1][col-1],col-1),(board[i+1][col-2],col-2)]
            else:
                r1val=[(board[i+1][r1],r1),(board[i+1][r1-1],r1-1),(board[i+1][r1+1],r1+1)]
            
            
            if r2==0:
                r2val=[(board[i+1][0],0),(board[i+1][1],1)]
            elif r2==col-1:
                r2val=[(board[i+1][col-1],col-1),(board[i+1][col-2],col-2)]
            else:
                r2val=[(board[i+1][r2],r2),(board[i+1][r2-1],r2-1),(board[i+1][r2+1],r2+1)]
                
            r1val.sort()
            r2val.sort()
            if r1val[-1][1]!=r2val[-1][1]:
                r1,r2=r1val[-1][1],r2val[-1][1]

            else:
                s1=r1val[-1][0]+r2val[-2][0]
                s2=r1val[-2][0]+r2val[-1][0]
                if s1<s2:
                    r1,r2=r1val[-2][1],r2val[-1][1]

                else:
                    r1,r2=r1val[-1][1],r2val[-2][1]
            print("i+1:{}".format(i+1))
            print("r1:{} ,r2:{}".format(r1,r2))

            cherry+=grid[i+1][r1]+grid[i+1][r2]
            
        return cherry
    
    
    
    """