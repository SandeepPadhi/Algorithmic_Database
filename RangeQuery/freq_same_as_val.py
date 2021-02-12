"""
Date:30/01/2021
The following program is solved using Fenwick Tree.

Given an array of N numbers, the task is to answer Q queries of the following type:-

query(start, end) = Number of times a 
number x occurs exactly x times in a 
subarray from start to end

"""

from collections import Counter
A = [1, 2, 2, 3, 3, 3 ,4]

F=[Counter()]
for a in A:
    F.append(Counter([a]))

def build():
    global F,A
    for idx in range(1,len(F)):
        idx2=idx+(idx&-idx)
        if idx2<len(F):
            F[idx2]+=F[idx]
def prefix(idx):
    idx+=1
    result=Counter()
    while(idx):
        result+=F[idx]
        idx-=(idx&-idx)
    return result

def query(l,r):
    Ans=dict(prefix(r)-prefix(l-1))
    R=[]
    for key,val in Ans.items():
        if key==val:
            R.append(key)
    return R
build()
print(query(1,6))

        

