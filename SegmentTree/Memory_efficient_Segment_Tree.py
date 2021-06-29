"""
Date:18/06/2021

The following is memory efficient Segment Tree which follows euler path indexing
rather than level order BFS indexing done tradionally.

This brings down memory requirement from 4N to 2N-1
"""


MAX=100000
N=10
Values=[i for i in range(N)]
S=[MAX]*(2*N +1)

def build(v,tl,tr):
    if tl==tr:
        S[v]=Values[tr]
        return 
    tm=(tl+tr)//2
    build(v+1,tl,tm)
    build(v+2*(tm-tl+1),tm+1,tr)
    S[v]=S[v+1]+S[v+2*(tm-tl+1)]

build(0,0,N-1)

def query(v,tl,tr,l,r):
    if l>r:
        return MAX
    if tl==l and tr==r:
        return S[v]
    tm=(tl+tr)//2
    v1=query(v+1,tl,tm,l,min(tm,r))
    v2=query(v+2(tm-tl+1),tm+1,tr,max(l,tm+1),r)
    return  min(v1,v2)

def update(v,tl,tr,pos,new_val):
    if tl==tr:
        S[v]=new_val
        Values[pos]=new_val
        return 
    tm=(tl+tr)//2
    if pos<=tm:
        update(v+1,tl,tm,pos,new_val)
    else:
        update(v+2*(tm-tl+1),tm+1,tr,pos,new_val)
    S[v]=S[v+1]+S[v+2*(tm-tl+1)]

