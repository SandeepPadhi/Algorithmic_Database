"""
Date:20/05/2021

The goal is to find no of elements in the connected components.
Link:https://www.geeksforgeeks.org/size-of-all-connected-non-empty-cells-of-a-matrix/?ref=rp

The following program is solved using DFS.
"""



A=[ [ 1, 1, 0, 0, 0 ],
            [ 1, 1, 0, 1, 1 ],
            [ 1, 0, 0, 1, 1 ],
            [ 1, 0, 0, 0, 0 ],
            [ 0, 0, 1, 1, 1 ] ]
M,N=len(A),len(A[0])

def dfs(i,j,count,A):
    if not (0<=i<M and 0<=j<N and A[i][j]==1):
        return
    count[0]+=1
    A[i][j]=0
    for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
        dfs(i+di,j+dj,count,A)



for i in range(M):
    for j in range(N):
        if A[i][j]:
            count=[0]
            dfs(i,j,count,A)
            print(count[0])