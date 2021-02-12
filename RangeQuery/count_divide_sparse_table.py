"""
Date:30/01/2021
Given N numbers and Q queries, each query consists of L and R. Task is to write a program 
which prints the count of numbers which divides all numbers in the given range L-R. 

Link:https://www.geeksforgeeks.org/count-elements-which-divide-all-numbers-in-range-l-r/

We have used Sparse Table\
\ ,where each node stores count,min and gcd of elements in the given range

"""


from collections import Counter

Arr = [2, 4,6,8,4,4,12,14,16,18,20] 
INF=10000
#We will implement a Sparse Table
Lookup=[[(Counter(),INF,0) for _ in range(5)] for _ in range(len(Arr)) ]

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

for i in range(len(Arr)):
    Lookup[i][0]=(Counter([Arr[i]]),Arr[i],Arr[i])
n=len(Arr)
j=1
while(1<<j <=n):
    i=0
    while(i+(1<<j)-1 <n):
        L1=Lookup[i][j-1]
        L2=Lookup[i+(1<<(j-1))][j-1]
        L=(L1[0]+L2[0],min(L1[1],L2[1]),gcd(L1[2],L2[2]))
        Lookup[i][j]=L
        i+=1
    j+=1

def query(l,r):
    import math
    if l>r:
        return (Counter(),INF,0)
    if l==r:
        return Lookup[l][0]
    j=int(math.log2(r-l+1))
    if 1<<j==(r-l+1):
        return Lookup[l][j]
    L1=Lookup[l][j]
    L2=Lookup[r-(1<<j)+1][j]
    L3=query(r-(1<<j)+1,l+(1<<j)-1)
    C=L1[0]+L2[0]-L3[0]
    return (C,min(L1[1],L2[1]),gcd(L1[2],L2[2]))
A=query(3,5)
if A[1]==A[2]:
    print("Ans is {} with count:{}".format(A[1],A[0][A[1]]))
else:
    print("No such number exists")
    