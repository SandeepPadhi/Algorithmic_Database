"""
Date:20/05/2021

The following program is implementation of Prims Algorithm.
Here,we connect cut edges
key[] = stores minimum cutedges to that vertices from mst to non-mst set

For N times:
    find V with min key value
    update the key values of Adj of V

Time-Complexity:O(V^2) using Adjacency Matrix
               :O(ElogV) using Adjacency List
"""

maxint=100000000000
graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]

Adj=[[] for _ in range(len(graph))]

for i in range(len(graph)):
    for j in  range(i+1,len(graph[0])):
        if graph[i][j]>0:
            Adj[i].append((j,graph[i][j]))
            Adj[j].append((i,graph[i][j]))


N=5
Parent=[None]*N
key=[maxint]*N
key[0]=0
mst=[False]*N
 
val=0
for _ in range(N):
    minval=maxint
    minind=-1
    for i in range(N):
         if not mst[i] and key[i]<minval:
             minval=key[i]
             minind=i
    val+=minval
    mst[minind]=True
    u=minind
    for v,w in Adj[u]:
        if not mst[v] and key[v]>w:
            Parent[v]=u
            key[v]=w
        

print(val)
print("Edges are:")
for u in range(N):
    print("u:{} , p:{}".format(u,Parent[u]))

  
