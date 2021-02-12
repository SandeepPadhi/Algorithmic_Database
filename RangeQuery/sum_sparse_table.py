"""
Date:24/01/2021 
The following problem is to find sum in range:[L,R]
It is solved using sparse Table
Sparse table is used when the table is static.That is ,there are not update operation
"""


import math

lookup=[[0 for _ in range(5)] for i in range(11)]


def preprocess(inp):
    global lookup
    n=len(inp)
    for i in range(n):
        lookup[i][0]=inp[i]
    
    j=1
    while(1<<j<=n):
        i=0
        while(i+(1<<j)-1 <n):
            lookup[i][j]=lookup[i][j-1]+lookup[i+(1<<(j-1))][j-1]
            i+=1
        j+=1

def query(l,r):
    if l>r:
        return 0
    if l==r:
        return lookup[l][0]
    j=int(math.log2(r-l+1))
    if r-l+1==1<<j:
        return lookup[l][j]
    return lookup[l][j]+lookup[r-(1<<j)+1][j]-query(r-(1<<j)+1,l+(1<<j)-1)


a = [7, 2, 3, 0, 5, 10, 3, 12, 18]
print("sum of a:{}".format(sum(a)))
preprocess(a)
n=len(a)
print("preprocessing done")
print("Query:(0,{})->{}".format(n-1,query(0,n-1)))
