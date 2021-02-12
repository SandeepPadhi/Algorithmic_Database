"""
Date:27/01/2021
IMPLEMENTATION OF SQRT DECOMPOSITION TECHNIQUE
TIME=O(SQRT(N)),SPACE=0(SQRT(N))
The following code is for find xor in range [L-R]
"""

import math
Arr=[0]*100
Block=[0]*100
blksize=0

def preprocess(inp):
    global Arr,Block,blksize
    n=len(inp)
    blksize=int(math.sqrt(n))
    blkindex=-1
    for i in range(n):
        Arr[i]=inp[i]
        if i%blksize==0:
            blkindex+=1
        Block[blkindex]^=Arr[i]

def update(index,val):
    global Block,Arr
    blkindex=index//blksize
    Block[blkindex]^=(Arr[index]^val)
    Arr[index]=val

def query(l,r):
    ans=0
    while(l<=r and l%blksize!=0):
        ans^=Arr[l]
        l+=1

    while(l+blksize-1<=r):
        ans^=Block[l//blksize]
        l+=blksize

    while(l<=r):
        ans^=Arr[l]
        l+=1
        
    return ans


input= [1, 5, 2, 4, 6, 1, 3, 5, 7, 10] 
n = len(input) 
  
preprocess(input) 
  
print("query(3,8) : ",query(3, 8)) 
print("query(1,6) : ",query(1, 6)) 
update(8, 0) 
print("query(8,8) : ",query(8, 8)) 
print("xor of index 3-8:{}".format(4^6^1^3^5^7))


