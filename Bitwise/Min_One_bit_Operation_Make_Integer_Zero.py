"""
Date:4/04/2021
1301. Number of Paths with Max Score - Leetcode Hard

The following problem is solved using DP
"""
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        board=[[int(b) if b.isnumeric() else -1 for b in boardrow ] for boardrow in board]
        Sum=[[0]*len(board[0]) for _ in range(len(board))]
        Path=[[0]*len(board[0]) for _ in range(len(board))]
        col=len(board[0])
        row=len(board)
        board[row-1][col-1]=0
        board[0][0]=0
        Path[-1][-1]=1
        mod=10**9 + 7
        #base condition done
        for i in range(col-2,-1,-1):
            if board[row-1][i]==-1:
                break
                Path[row-1][i]=0
                Sum[row-1][i]=0
            else:
                Path[row-1][i]=1
                Sum[row-1][i]=Sum[row-1][i+1]+board[row-1][i]
            
            
        for i in range(row-2,-1,-1):
            if board[i][col-1]==-1:
                Path[i][col-1]=0
                Sum[i][col-1]=0
                break
            else:
                Path[i][col-1]=1
                Sum[i][col-1]=Sum[i+1][col-1]+board[i][col-1]
        
        
        
        for r in range(row-2,-1,-1):
            for c in range(col-2,-1,-1):
                v=board[r][c]
                if v==-1:
                    continue
                else:
                    C=Counter()
                    maxval=-1
                    maxdir=-1
                    #down
                    if board[r+1][c]!=-1:
                        maxval=max(maxval,Sum[r+1][c])
                        maxdir=max(maxdir,board[r+1][c])

                        #print(Sum[r+1][c])
                        #print(C)
                        C[Sum[r+1][c]]+=1
                    
                    if board[r+1][c+1]!=-1:
                        maxval=max(maxval,Sum[r+1][c+1])
                        maxdir=max(maxdir,board[r+1][c+1])
                        C[Sum[r+1][c+1]]+=1
                    if board[r][c+1]!=-1:
                        maxval=max(maxval,Sum[r][c+1])
                        maxdir=max(maxdir,board[r][c+1])

                        C[Sum[r][c+1]]+=1
                       
                    if maxdir!=0 and (len(C)==0 or maxval==0):
                        continue

                        
                    #print("maxdir:{},maxval:{}".format(maxdir,maxval))
   
                    Sum[r][c]=int(board[r][c])+maxval
                    
                    if board[r+1][c]!=-1 and Sum[r+1][c]==maxval:
                        Path[r][c]+=Path[r+1][c]                    
                    
                    if board[r+1][c+1]!=-1 and Sum[r+1][c+1]==maxval:
                        Path[r][c]+=Path[r+1][c+1]   
                        
                    if board[r][c+1]!=-1 and Sum[r][c+1]==maxval:
                        Path[r][c]+=Path[r][c+1]
                    
                    #Path[r][c]=C[maxval]
                Path[r][c]%=mod
                Sum[r][c]%=mod
        
        #print(Sum)
        
        #print()
        #print(Path)
        return [Sum[0][0]%mod,Path[0][0]%mod]
        