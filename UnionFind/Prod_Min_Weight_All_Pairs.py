"""
Product of minimum edge weight between all pairs of a Tree
Difficulty Level : Hard
Given a tree with N vertices and N-1 Edges. Let’s define a function F(a, b) which is equal to the minimum edge weight in the path between node a & b. The task is to calculate the product of all such F(a, b)

Link:https://www.geeksforgeeks.org/product-of-minimum-edge-weight-between-all-pairs-of-a-tree/

"""


from functools import cmp_to_key
mod=10**9 + 7
Edges=[[1,2,1],[1,3,3],[4,3,2],[1,5,4]]

def compare(a,b):
    if a[-1]<b[-1]:
        return 1
    else:
        return -1

Edges.sort(key=cmp_to_key(compare))
print(Edges)

P=[i for i in range(8)]
S=[1 for i in range(8)]

def find(p):
    if P[p]!=p:
        P[p]=find(P[p])
    return P[p]


result=1
for u,v,w in Edges:
    pu=find(u)
    pv=find(v)
    sizeu=S[pu]
    sizev=S[pv]
    print("u:{} , v:{} , sizeu:{} , sizev:{}".format(u,v,sizeu,sizev))
    if sizeu<sizev:
        P[pu]=pv
        S[pv]+=sizeu
    else:
        P[pv]=pu
        S[pu]+=sizev
    
    prod=sizeu*sizev
    product=pow(w,prod,mod)
    result=(product*result)%mod

print(result)
    



