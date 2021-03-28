# cook your dish here

"""
Following problem checks if the graph is Bipartite or not using two coloring method
We make use of & and ^ operator to accomplish our purpose

The number of ways to color a bipartite graph is 2^C ,where C=No of connected components

"""

from collections import deque
Edges=[(1,4),(1,6),(2,6),(2,4),(2,5),(2,7),(3,6),(3,7),(8,9)]
V=9
Adj=[[] for _ in range(V+1)]
for u,v in Edges:
    Adj[v].append(u)
    Adj[u].append(v)

isbipartite=True
Side=[-1]*(V+1)
Q=deque()
for i in range(1,V+1):
    if Side[i]==-1:
        Side[i]=0
        Q.append(i)
        while(len(Q)):
            u=Q.popleft()
            for v in Adj[u]:
                if Side[v]==-1:
                    Side[v]=Side[u]^1
                    Q.append(v)
                else:
                    isbipartite=(Side[v]!=Side[u])
                    
print("Side:{}".format(Side))
print("Bipartite:{}".format("Yes" if isbipartite else "No"))