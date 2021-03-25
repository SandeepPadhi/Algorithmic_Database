"""
Date:24/01/2021
1) Only for DAG can we find longest path using Bellman Ford Algo for shortest path.
2) Here ,we first use Kahn's Topological Sort Algorithn to find if there is negative length
   cycle in the DAG.
3) After that we check for negative cycle.
4) If not found then,we apply Bellman Ford algorithm with edge weights reversed.
5) At the same we also store the path using parent List

"""

from collections import deque

# Here edge=(u,v,weight) u->v
edges = [(0, 6, 2), (1, 2, -4), (1, 4, 1), (1, 6, 8), (3, 0, 3),
         (3, 4, 5), (5, 1, 2), (7, 0, 6), (7, 1, -1), (7, 3, 4), (7, 5, -4)]

V = 8
Adj = [[] for _ in range(V)]
Indegree = [0]*V
Result = []
for u, v, w in edges:
    Adj[u].append(v)
    Indegree[v] += 1
print("Indegree before:{}".format(Indegree))
S = []
for i in range(V):
    if Indegree[i] == 0:
        S.append(i)
        
sources = deque(S)
while(sources):
    m = sources.pop()
    for v in Adj[m]:
        Indegree[v] -= 1
        if Indegree[v] == 0:
            sources.append(v)

print("Indegre:{}".format(Indegree))
for i in Indegree:
    if i != 0:
        print("Cycle found not possible")
INF = 10000000
dist = [INF]*V
for s in S:
    dist[s] = 0
parent = [i for i in range(V)]
for _ in range(V-1):
    for u, v, w in edges:
        if dist[u] != INF and dist[u]-w < dist[v]:
            dist[v] = dist[u]-w
            parent[v] = u

print("dist:{}".format(dist))
minindex = 0
minval = INF
for i in range(V):
    if dist[i] < minval:
        minval = dist[i]
        minindex = i

path = [minindex]
i = minindex
while parent[i] != i:
    m = parent[i]
    path.append(m)
    i = m
path.reverse()
print("path:{}".format(path))
