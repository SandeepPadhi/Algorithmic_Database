"""
Date:27/01/2021
The following program is implementation of sparse Table for finding min in range [L,R]
"""

import math
INF=100000
#look[index][j],where j represents size in powers of 2 and j represents power
lookup=[[INF for _ in range(100)] for _ in range(100)]

def preprocess(inp):
    global lookup
    n=len(inp)
    for i in range(n):
        lookup[i][0]=inp[i]
    j=1
    while(1<<j <=n):
        i=0
        while(i+(1<<j)-1<n):
            lookup[i][j]=min(lookup[i][j-1],lookup[i+1<<(j-1)][j-1])
            i+=1
        j+=1
def query(l,r):
    j=int(math.log2(r-l+1))
    print("j:{}".format(j))
    return min(lookup[l][j],lookup[r-(1<<j)+1][j])

a = [7, 2, 3, 1, 5, 10, 3, 12, 18]
n = len(a)
preprocess(a)
q1=query(0, 4)
print("min of (0,4):{}".format(q1))
q2=query(4, 7)
print("min of (4,7):{}".format(q2))

q3=query(7, 8)
print("min of (7,8):{}".format(q3))


