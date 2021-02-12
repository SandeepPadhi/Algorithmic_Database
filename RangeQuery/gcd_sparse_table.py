"""
Date:27/01/2021
The following problem is find GCD of range: [L,R]
This is solved by sparse Table.
Sparse Table is used when the table is static i.e there are no update operation.
"""


import math

lookup=[[1 for _ in range(5)] for _ in range(12)]

def preprocess(inp):
    global lookup
    n=len(inp)
    for i in range(n):
        lookup[i][0]=inp[i]
    j=1
    while(i<<j <=n):
        i==0
        while(i+(1<<j)-1<=n):
            lookup[i][j]=math.gcd(lookup[i][j-1],lookup[i+(1<<(j-1))-1][j-1])
            i+=1
        j+=1
def query(l,r):
    j=int(math.log2(r-l+1))
    return math.gcd(lookup[l][j],lookup[r-(1<<j)+1][j])


a = [7, 2, 3, 0, 5, 10, 3, 12, 18]
g=7
for i in range(4,len(a)):
    g=math.gcd(g,a[i])
print("gcd of a:{}".format(g))
preprocess(a)
n=len(a)
print("preprocessing done")
print("Query:(4,{})->{}".format(n-1,query(4,n-1)))
