#code
"""
Date:2/02/2021
The following program finds if characters in the string can be rearranged in away such
that no two adjacent characters are same.

Link:https://practice.geeksforgeeks.org/problems/rearrange-characters/0#
"""

def solve():
    from collections import defaultdict
    import heapq
    Str=[s for s in input()]
    Count=defaultdict(lambda:0)
    for s in Str:
        Count[s]+=1
    H=[]
    for key,val in Count.items():
        heapq.heappush(H,(-val,key))
    
    val,key=heapq.heappop(H)
    Cat=[[] for _ in range(-val)]
    L=-val
    i=0
    while(H):
        val,key=heapq.heappop(H)
        for v in range(-val):
            Cat[i].append(key)
            i=(i+1)%L
    if len(Cat)==1:
        print("0")
        return 0
    if len(Cat[-1])==0 and len(Cat[-2])==0:
        print("0")
        return 0
    print("1")
    return 1
        
    
    
    
    
T=int(input())
for _ in range(T):
    solve()