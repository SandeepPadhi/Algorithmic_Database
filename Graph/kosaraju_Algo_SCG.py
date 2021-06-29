
"""
Date:3/02/2021
The following program is to find if graph is Strongly Connected.
It is called Kosaraju's Algorithm.
"""

Edges=[(3,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,4)]
Adj=[[] for i in range(10)]
for u,v in Edges:
    Adj[u].append(v)
V=[False]*7
def dfs(u):
    global V
    V[u]=True
    for v in Adj[u]:
        if V[v]==False:
            dfs(v)
dfs(1)
for i in range(1,7):
    if V[i]==False:
        print("Not connected")
        break

Rev=[[] for i in range(10)]
for u,v in Edges:
    Rev[v].append(u)
V=[False]*7
def dfsr(u):
    global V
    V[u]=True
    for v in Rev[u]:
        if V[v]==False:
            dfsr(v)
dfsr(1)
for i in range(1,7):
    if V[i]==False:
        print("Not connected")
        break
print("connected")