"""
Date:2/01/2021
The following code is solved using Queue and BFS
"""
class Solution:
    	def orangesRotting(self, grid):
		#Code here
		from collections import deque
		n,m=len(grid),len(grid[0])
		INF=1000
		time=[[INF if grid[i][j]!=2 else 0 for j in range(m)] for i in range(n)]
		#We will use bfs to solve this
		Q=deque()
		for i in range(n):
		    for j in range(m):
		        if grid[i][j]==2:
		            Q.append((i,j))
		T=0
		while(Q):
		    x,y=Q.popleft()
		    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
		        nx,ny=x+dx,y+dy
		        if nx<n and ny<m and nx>=0 and ny>=0 and grid[nx][ny]==1 and time[nx][ny]>time[x][y]+1:
		            grid[nx][ny]=2
		            time[nx][ny]=time[x][y]+1
		            T=max(T,time[nx][ny])
		            
		            Q.append((nx,ny))
		            
		
		
		for i in range(n):
		    for j in range(m):
		        if grid[i][j]==1:
		            return -1
	
		return T


#{ 
#  Driver Code Starts
from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends