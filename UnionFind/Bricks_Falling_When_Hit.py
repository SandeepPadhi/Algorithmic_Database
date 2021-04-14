"""
Date:13/04/2021
803. Bricks Falling When Hit - Leetcode Hard

The following problem is solved using Union Find
"""

class DSU:
    def __init__(self,m,n):
        self.parent=list(range(m*n+1))
        self.rank=[0]*(m*n+1)
        self.size=[1]*(m*n+1)
        self.size[0]=0   
        
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
        
    def union(self,x,y):
        p1=self.find(x)
        p2=self.find(y)
        if p1!=p2:
            if self.rank[p1]>self.rank[p2]:
                self.parent[p2]=p1
                self.size[p1]+=self.size[p2]
            elif self.rank[p2]>self.rank[p1]:
                self.parent[p1]=p2
                self.size[p2]+=self.size[p1]
            else:
                self.parent[p1]=p2
                self.size[p2]+=self.size[p1]
                self.rank[p2]+=1
        
        
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m=len(grid)
        n=len(grid[0])
        dsu=DSU(m,n)
        for x,y in hits:
            if grid[x][y]==1:
                grid[x][y]=2
        
        #print("grid:{}".format(grid))
        
        direction=[(-1,0),(1,0),(0,1),(0,-1)]
        
        def doUnion(i,j):
            seq1=i*n+j+1
            for di,dj in direction:
                ni,nj=i+di,j+dj
                if 0<=ni<m and 0<=nj<n and grid[ni][nj]==1:
                    seq2=ni*n+nj+1
                    dsu.union(seq1,seq2)
            if i==0:
                dsu.union(0,seq1)
                    
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    doUnion(i,j)
        
        #print("parent:{}".format(dsu.parent))
        #print("size:{}".format(dsu.size))
        Res=[0]*len(hits)
        countRootbricks=dsu.size[dsu.find(0)]
        for i in range(len(hits)-1,-1,-1):
            x,y=hits[i][0],hits[i][1]
            if grid[x][y]==2:
                grid[x][y]=1
                doUnion(x,y)
                newBrickCount=dsu.size[dsu.find(0)]
                if newBrickCount>countRootbricks:
                    Res[i]=newBrickCount-countRootbricks-1
                    countRootbricks=newBrickCount
        #print("bricks:{}".format(dsu.size[dsu.find(0)]))
        #print("size:{}".format(dsu.size))
        #print("parent:{}".format(dsu.parent))
        #print("parent of 0:{}".format(dsu.find(0)))
        return Res
                
        
                
"""
"""
"""
Date:13/04/2021
803. Bricks Falling When Hit - Leetcode Hard

The following problem is solved using BFS..but gives TLE
"""
"""
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        Result=[0]*len(hits)
        row,col=len(grid),len(grid[0])
        ind=0
        
        def calculate(grid,queue,Visited,Result,path,ind):
            #print("Ind:{}".format(ind))
            #print("queue:{}".format(queue))
            Done=True
            while(queue):
                gx,gy=queue.popleft()
                
                if gx==0:
                    Done=False
                    break
                
                path.append((gx,gy))
                        
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx,ny=gx+dx,gy+dy
                    if (nx,ny) not in Visited and 0<=nx<row and 0<=ny<col and grid[nx][ny]==1:
                        Visited.add((nx,ny))
                        queue.append((nx,ny))
            if Done:
                Result[ind]+=(len(path))
                #print("path:{}".format(path))
                #print("added:{}".format(len(path)))
                for gx,gy in path:
                    grid[gx][gy]=0
               
            
        
        
        for x,y in hits:
            
            if grid[x][y]==1:
                #print("x:{} , y:{}".format(x,y))
                grid[x][y]=0
                #up
                if x-1>=0 and grid[x-1][y]==1:
                    path=[]
                    queue=[(x-1,y)]
                    queue=deque(queue)
                    Visited=set()
                    Visited.add((x-1,y))
                    calculate(grid,queue,Visited,Result,path,ind)
                if x+1<row and grid[x+1][y]==1:
                    path=[]
                    queue=[(x+1,y)]
                    queue=deque(queue)
                    Visited=set()
                    Visited.add((x+1,y))
                    calculate(grid,queue,Visited,Result,path,ind)
                if y-1>=0 and grid[x][y-1]==1:
                    path=[]
                    queue=[(x,y-1)]
                    queue=deque(queue)
                    Visited=set()
                    Visited.add((x,y-1))
                    calculate(grid,queue,Visited,Result,path,ind)
                if y+1<col and grid[x][y+1]==1:
                    path=[]
                    queue=[(x,y+1)]
                    queue=deque(queue)
                    Visited=set()
                    Visited.add((x,y+1))
                    calculate(grid,queue,Visited,Result,path,ind)                
                    
            ind+=1
        #print("grid:{}".format(grid))
        return Result
                
                
                


"""
                