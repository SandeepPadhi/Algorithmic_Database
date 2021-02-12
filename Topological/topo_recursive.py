from collections import deque

edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]
V=8
Adj=[[] for _ in range(V)]
Indegree=[0]*V
Discovered=[False]*V
Result=[]

for u,v in edges:
    Adj[u].append(v)
    Indegree[v]+=1

def topologicalsort(Result,Indegree,Discovered):
    if len(Result)==V:
        return
    for u  in range(V):
        if Indegree[u]==0 and not Discovered[u]:
            Discovered[u]=True
            for v in Adj[u]:
                Indegree[v]-=1
            Result.append(u)
            topologicalsort(Result,Indegree,Discovered)
            break
topologicalsort(Result,Indegree,Discovered)
print("Result:{}".format(Result))
    