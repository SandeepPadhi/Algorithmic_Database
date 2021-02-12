"""
Following code is used for finding min in range L-R.
The section for update is important here

"""


import math
MAX=100000
Block=[MAX]*100
Arr=[0]*100
blksize=0

def preprocess(inp):
    global blksize,Block,Arr
    n=len(inp)
    blksize=int(math.sqrt(n))
    blkindex=-1
    for i in range(n):
        Arr[i]=inp[i]
        if i%blksize==0:
            blkindex+=1
        Block[blkindex]=min(Block[blkindex],Arr[i])

def update(index,val):
    global Block,Arr
    blkindex=index//blksize
    Block[blkindex]=min(query(blkindex*blksize,index-1),val,query(index+1,blkindex*blksize + blksize-1))
    Arr[index]=val
    
def query(l,r):
    if l>r:
        return MAX
    ans=MAX
    while(l<=r and l%blksize!=0):
        ans=min(ans,Arr[l])
        l+=1
    while(l<=r and l+blksize-1<=r):
        ans=min(ans,Block[l//blksize])
        l+=blksize
    while(l<=r):
        ans=min(ans,Arr[l])
        l+=1
    return ans

input= [1, 5, 2, 4, 6, 1, 3, 5, 7, 10] 
n = len(input) 
 
preprocess(input) 
  
print("query(1,4) : ",query(1, 4)) 
print("query(1,6) : ",query(1, 6)) 
update(3, 1.5) 
print("query(1,4 : ",query(1, 4)) 

    
    
