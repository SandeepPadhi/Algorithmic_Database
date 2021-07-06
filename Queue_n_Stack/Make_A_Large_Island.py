"""
Date:30/06/2021
827. Making A Large Island - Leetcode Hard

The following program is solved using BFS
"""
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        Count={}
        comp=2
        Ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    queue=deque()
                    queue.append((i,j))
                    grid[i][j]=comp
                    count=1
                    while(queue):
                        x,y=queue.popleft()
                        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<n and 0<=ny<m and grid[nx][ny]==1:
                                grid[nx][ny]=comp
                                count+=1
                                queue.append((nx,ny))
                    
                    Count[comp]=count
                    comp+=1
                    Ans=max(Ans,count)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    S=set()
                    for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                        ni,nj=i+di,j+dj
                        if 0<=ni<n and 0<=nj<m and grid[ni][nj]>0:
                            S.add(grid[ni][nj])
                    
                    val=1
                    for s in S:
                        val+=Count[s]
                    Ans=max(val,Ans)
        
        return Ans
                            
        
        