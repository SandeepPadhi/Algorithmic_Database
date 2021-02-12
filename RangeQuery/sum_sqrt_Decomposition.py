"""
Date:27/01/2021
The following code is solved using Sqrt Decompostion Technique for range query.
It gives sum of element in range [L,R]
"""

import math
Arr=[0]*10
Block=[0]*10
blksize=0


def preprocess(inp):
    global Block,blksize,Arr
    n=len(inp)
    blksize=int(math.sqrt(n))
    blkindex=-1
    print("blksize:{}".format(blksize))
    for i in range(n):
        Arr[i]=inp[i]
        if i%blksize==0:
            blkindex+=1
        Block[blkindex]+=inp[i]

def update(index,val):
    global Block,Arr
    blkindex=index//blksize
    Block[blkindex]+=val-Arr[index]
    Arr[index]=val
def query(l,r):
    ans=0
    while(l<=r and l%blksize!=0):
        
        ans+=Arr[l]
        l+=1
    while(l+blksize-1<=r):
        ans+=Block[l//blksize]
        l+=blksize
    while(l<=r):
        ans+=Arr[l]
        l+=1
    return ans
    
input= [1, 5, 2, 4, 6, 1, 3, 5, 7, 10] 
n = len(input) 
  
preprocess(input) 
print("Arr:{}".format(Arr))
print("query(3,8) : ",query(3, 8)) 
print("query(1,6) : ",query(1, 6)) 
update(8, 0) 
print("query(8,8) : ",query(8, 8)) 
        
        