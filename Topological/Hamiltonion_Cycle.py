"""
Date:24/01/2021
Hamiltonion Cycle is NP-Complete Problem .Hence,no Polynomial time solution exists for it.
It is solved using Backtracking.

The following program print all possible Hamiltanion paths.
It also tries to find if hamiltonion cycle exists or not
"""




edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
V=4
Adj=[[] for _ in range(V)]
for u,v in edges:
    Adj[u].append(v)
    Adj[v].append(u)


def Hamiltanion(path,u,visited):
    if len(path)==V:
        print("Path:{}".format(path))
        if path[0] in Adj[path[-1]]:
            print("It is also Hamiltonion cycle")
        return
    for v in Adj[u]:
        if visited[v]==False:
            path.append(v)
            visited[v]=True
            Hamiltanion(path,v,visited)
            visited[v]=False
            path.pop()
for source in range(V):
    visited=[False]*V
    visited[source]=True
    path=[source]
    Hamiltanion(path,source,visited)
            


