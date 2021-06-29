"""
Date:3/02/2021

The following program is for findiing all strongly connected Components.
It is called Kosaraju's Algorithm for finding Strongly Connected Components

Time Complexity:O(V+E)
It uses two DFS

"""

Edges=[(3,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,4)]
N=7
Adj=[[] for _ in range(7)]
for u,v in Edges:
    Adj[u].append(v)

#DFS on actual edges and storing vertices as per their departure time    
P=[]
def dfs(u):
    global V,P
    V[u]=True
    for v in Adj[u]:
        if V[v]==False:
            dfs(v)
    P.append(u)#We are storing vertices at their departure

V=[False]*N
for i in range(1,N):
    if V[i]==False:
        dfs(i)

#Reversing the graph and doing DFS
def dfsr(u,P):
    global V
    V[u]=True
    P.append(u)
    for v in Rev[u]:
        if V[v]==False:
            dfsr(v,P)

Rev=[[] for _ in range(N)]
for u,v in Edges:
    Rev[v].append(u)
V=[False]*N
Result=[]

#We call dfsr till P is empty.Vertices are called as per their
#Departure timing.
#Hence ,stack is used
while(P):
    u=P.pop()
    if V[u]==True:
        continue
    Path=[]
    dfsr(u,Path)
    Result.append(Path)
    
print("Result:{}".format(Result))
    
    

    