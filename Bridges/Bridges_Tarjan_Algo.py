"""
Date:28/01/2021
Following code is for finding Bridges using Tarjan's Algo
Following Arrays are used:
Disc-stores discovery time.
Low-discovery time earliest visited anscestors including itself.
Result-Stores past results.
"""
Edges=[(3,5),(3,4),(5,2),(6,5),(6,7),(7,2),(2,1),(4,2),(1,9)]
V=0
for u,v in Edges:
    V=max(V,u,v)
Adj=[[] for _ in range(V+1)]
for u,v in Edges:
    Adj[u].append(v)
    Adj[v].append(u)

Result=[]
Visited=[False]*(V+1)
INF=1000
Disc=[INF]*(V+1)
Low=[INF]*(V+1)
Parent=[i for i in range(V+1)]
time=0
Result=[]

def Bridge(u):
    global Visited,Disc,Low,Parent,Result,time
    Visited[u]=True
    Disc[u]=time
    Low[u]=time
    time+=1
    
    for v in Adj[u]:
        if Visited[v]==False:
            Parent[v]=u
            Bridge(v)
            Low[u]=min(Low[u],Low[v])
            if Disc[u]<Low[v]:
                Result.append((u,v))
        
        elif Parent[u]!=v:
            Low[u]=min(Low[u],Disc[v])
    

for i in range(1,V+1):
    if Visited[i]==False:
        Bridge(i)
print("Result:{}".format(Result))