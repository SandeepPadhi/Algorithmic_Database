"""
Date:28/01/2021
The following code is to find diameter of N-ary general Tree
"""

Edges=[(1,2),(2,3),(2,4),(4,5),(5,6),(4,7),(7,8),(8,9),(1,10),(10,11),(10,12),(10,13),(13,14)]

V=0
for u,v in Edges:
    V=max(V,u,v)
Adj=[[] for _ in range(V+1)]
for u,v in Edges:
    Adj[u].append(v)
    Adj[v].append(u)

root=2
Visited=[False]*(V+1)
def diameter(u):
    global Visited
    Visited[u]=True
    CH=[]
    CD=[]
    
    for v in Adj[u]:
        if Visited[v]==True:
            continue
        h,d=diameter(v)
        CH.append(h)
        CD.append(d)
    CH.sort()
    CD.sort()
    if len(CH)==0:
        print("Leaf:{}".format(u))
        return 1,1
    if len(CH)==1:
        print("depth of 1:{}".format(u))
        return CH[0]+1,max(CD[0],CH[0]+1)
        
    return CH[-1]+1,max(CD[-1],CH[-1]+CH[-2]+1)



D=diameter(root)#Height of root,Diameter of Tree
print("Adj:{}".format(Adj))
print("Diameter of D:{}".format(D))