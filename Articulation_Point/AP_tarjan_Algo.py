"""
Date:28/01/2021
Following is the implementation of Tarjan's Algorithm.Basically,it is DFS with additional code

Link:https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/

Leaf nodes can never be articulation points.
A root node can be AP if it has at least two children
A non-root node can AP if at least one subtree of node does not
have a backedge to the ancestor of that node.

But that ancestor cannot be parent of that node

Here,Disc=stores discovery time of the node
     Low[u]=min(Disc[u],Disc[v])i.e min of discovery time of child and that of any of the 
                                    ancestors to which the substree has backedge.
                                    This disc time is passed to the child by backtracking
"""
#Edges=[(1,2),(2,4),(2,5),(1,3),(3,6),(3,7),(2,8),(5,8),(4,8),(5,3)]
#Edges=[(9,4),(4,2),(4,1),(2,8),(1,8),(9,7),(9,6),(6,5),(7,5),(5,3)]
Edges=[(1,2),(2,3),(3,1)]
V=0
for E in Edges:
    V=max(V,E[0],E[1])
print("V:{}".format(V))
Adj=[[] for _ in range(V+1)]
for u,v in Edges:
    Adj[u].append(v)
    Adj[v].append(u)

Parent=[-1]*(V+1)
INF=1000
Disc=[INF]*(V+1)
Low=[INF]*(V+1)
Visited=[False]*(V+1)
time=0
result=set()

def AP(u):
    global Visited,Disc,Low,Parent,time,result
    Visited[u]=True
    Disc[u]=time
    Low[u]=time
    time+=1
    children=0
    for v in Adj[u]:
        if Visited[v]==False:
            children+=1
            Parent[v]=u
            AP(v)
            Low[u]=min(Low[u],Low[v])
            
            if Parent[u]==-1 and children>1:
                result.add(u)
            if Parent[u]!=-1 and Disc[u]<=Low[v]:#equal to because a cycle may start and end at the node
                result.add(u)
                
            
        elif v!=Parent[u]:
            Low[u]=min(Low[u],Disc[v])
    

for i in range(1,V+1):
    if Visited[i]==False:
        AP(i)
print("Articulation Points are {}".format(result))




