"""
Date:23/03/2021
F. Graph Without Long Directed Paths  - CodeForces - Codeforces Round #550 (Div. 3)

The following problem is solved using concepts of Bipartite Graph
"""


import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd,deque
from bisect import bisect_left as bl,bisect_right as br


sys.setrecursionlimit(100000000)

inp    =lambda: int(input())
strng  =lambda: input().strip()
jn     =lambda x,l: x.join(map(str,l))
strl   =lambda: list(input().strip())
mul    =lambda: map(int,input().strip().split())
mulf   =lambda: map(float,input().strip().split())
seq    =lambda: list(map(int,input().strip().split()))

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

flush  =lambda: stdout.flush()
stdstr =lambda: stdin.readline()
stdint =lambda: int(stdin.readline())
stdpr  =lambda x: stdout.write(str(x))

mod=1000000007


n,m=mul()
#print("m:{},n:{}".format(m,n))
Adj=[[] for _ in range(n+1)]
Edges=[]
for _ in range(m):
    u,v = mul()
    Edges.append((u,v))
    Adj[u].append(v)
    Adj[v].append(u)
#print("Adj:{}".format(Adj))

Side=[-1]*(n+1)
Q=deque()
isbipartite=True
for i in range(1,n+1):
    if Side[i]==-1:
        Q.append(i)
        Side[i]=1
        while(len(Q)):
            u=Q.pop()
            for v in Adj[u]:
                if Side[v]==-1:
                    Side[v]=Side[u]^1
                    Q.append(v)
                else:
                    isbipartite&=Side[v]!=Side[u]

if not isbipartite:
    print("NO")
else:
    #print("Side:{}".format(Side))
    print("YES")
    S=""
    for u,v in Edges:
        if Side[u]==0:
            S+="0"
        else:
            S+="1"
    print(S)
            
    