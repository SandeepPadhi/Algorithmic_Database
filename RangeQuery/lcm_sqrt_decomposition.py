S = [2, 8, 6, 9, 8, 6, 8, 2, 11,8,7] 
#We will solve this using sqrt decomposition technique
Block=[1]*len(S)
blksize=-1
import math
def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def lcm(a,b):
    return a*b//(gcd(a,b))

def preprocess():
    global Block,blksize
    blksize=int(math.sqrt(len(S)))
    blkindex=-1
    for i in range(len(S)):
        if i%blksize==0:
            blkindex+=1
        Block[blkindex]=lcm(Block[blkindex],S[i])

def query(l,r):
    ans=1
    while(l<=r and l%blksize!=0):
        ans=lcm(ans,S[l])
        l+=1
    while(l+blksize-1<=r):
        
        ans=lcm(ans,Block[l//blksize])
        l+=blksize
    while(l<=r):
        ans=lcm(ans,S[l])
        l+=1
    return ans

def update(index,val):
    global Block,S
    j=index//blksize
    l=blksize*j
    r=l+blksize-1
    S[index]=val
    ans=1
    for i in range(l,r+1):
        ans=lcm(ans,S[i])
    Block[j]=ans
    
    
preprocess()
print(query(0,len(S)-1))
    
