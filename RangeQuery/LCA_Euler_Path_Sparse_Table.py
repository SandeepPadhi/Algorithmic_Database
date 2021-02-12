"""
Date:27/01/2021
Here,E stores path of DFS and L stores the corresponding level
Here,H stores the first time DFS encountered a particular node

Whenever LCA of two nodes are asked to find out,we first find indexes of using H ,
and then find the index of E betwwen those indices where L is lowest.

That index gives LCA

Here,we use sparse tree to LCA between two range.

We,build every thing using edges,then parent,child ,then Sparse Tree

"""


edges=[(3,2),(2,5),(2,1),(3,7),(7,4),(7,6)]
Parent=[i for i in range(8)]
Child=[[] for _ in range(8)]
for u,v in edges:
    Parent[v]=u
    Child[u].append(v)

H=[0 for _ in range(8)]
E=[0]
L=[0]
#Finding root
def findroot(Parent):
    for i in range(1,len(Parent)):
        if Parent[i]==i:
            return i
    return -1

#DFS
def dfs(root,E,L,H,level):
    if root==None:
        return
    L.append(level)
    E.append(root)
    H[root]=len(E)-1
    
    for c in Child[root]:
        dfs(c,E,L,H,level+1)
        L.append(level)
        E.append(root)
root=findroot(Parent)

print("Root is :{}".format(root))
dfs(root,E,L,H,1)
print("E:{}".format(E))
print("L:{}".format(L))
print("H:{}".format(H))


Lookup=[[(0,100)for _ in range(10)] for _ in range(10*len(E))]

def preprocess(E,L):
    global Lookup
    for i in range(len(E)):
        Lookup[i][0]=(E[i],L[i])
    n=len(E)
    print("n:{}".format(n))
    j=1
    while(1<<j <=n):
        i=0
        while(i+(1<<j)-1<n):
            
            L1=Lookup[i][j-1]
            L2=Lookup[i+(1<<(j-1))][j-1]
            #print("L1:{} ,L2:{}".format(L1,L2))
            if L1[1]<L2[1]:
                Lookup[i][j]=L1
            else:
                Lookup[i][j]=L2
            i+=1
        j+=1

def query(n1,n2,H):
    import math
    l=H[n1]
    r=H[n2]
    #print("l:{},r:{}".format(l,r))
    if l>r:
        l,r=r,l
    j=int(math.log2(r-l+1))
    L1=Lookup[l][j]
    L2=Lookup[r-(1<<j)+1][j]
    #print("L1:{},L2:{}".format(L1,L2))
    if L1[1]<=L2[1]:
        return L1[0]
    return L2[0]
    
preprocess(E,L)
print("LCA of (2,1):{}".format(query(2,1,H)))
print("LCA of (2,6):{}".format(query(2,6,H)))
print("LCA of (4,1):{}".format(query(4,1,H)))
print("LCA of (3,4):{}".format(query(3,4,H)))


    
