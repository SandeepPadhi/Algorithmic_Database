"""
Date:28/04/2021
LOWEST_COMMON_ANCESTOR - Using Binary Lifting

The following program is solved using Binary Lifting .Its implemented using DFS for updating "up" array
"""


import math
P=[0 ,0, 1, 1, 2, 2, 3, 3]
 #|0 1 2 3 4 5 6 7 |8 9
root=0

N=len(P)
Adj=[[] for _ in range(N+1)]
for i in range(len(P)):
    child=i
    parent=P[child]
    Adj[parent].append(child)
Adj[root].remove(root)


LOG = 0
for i in range(32,-1,-1):
    if N&(1<<i):
        LOG=i
        break
LOG+=3
#print("LOG:{}".format(LOG))
up=[[0]*LOG  for _ in range(N+1)]
depth=[0]*(N+1)
print("Adj:{}".format(Adj))
def dfs(root):
    for child in Adj[root]:
        depth[child]=depth[root]+1
        up[child][0]=root
        temp=child
        for i in range(1,LOG):
            #print(i)
            up[temp][i]=up[up[temp][i-1]][i-1]
        dfs(child)
dfs(root)
#print(up[4][5])

def lca(p,q):
    if depth[p]<depth[q]:
        p,q=q,p
    k=depth[p]-depth[q]
    for i in range(LOG):
        if k&(1<<i):
            p=up[p][i]
    if p==q:
        return p
    for i in range(LOG-1,-1,-1):
        while(up[p][i]!=up[q][i]):
            p=up[p][i]
            q=up[q][i]
            
    
    
    return up[p][0]
    
    


p=5
q=4
ans=lca(p,q)
print(ans)



        
    