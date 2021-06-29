"""
Date:22/05/2021
Problem:Find the numbers of strings that can be formed after processing Q queries

Link:https://www.geeksforgeeks.org/find-the-numbers-of-strings-that-can-be-formed-after-processing-q-queries/
Following problem is solved using Union - Find
"""


n = 4
P=[i for i in range(n+1)]

def findParent(p):
    global P
    if P[p]!=p:
        P[p]=findParent(P[p])
    return P[p]

def query(low,high):
    while(low<high):
        plow=findParent(low)
        phigh=findParent(high)
        P[low]=phigh
        low+=1
        high-=1


# queries
query(1, 3)
query(2, 4)

for p in range(len(P)):
    P[p]=findParent(p)

v=len(set(P))-1
ans=26**v
print(ans)
print(P)

