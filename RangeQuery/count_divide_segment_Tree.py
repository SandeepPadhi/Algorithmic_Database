"""
Date:30/01/2021
Given N numbers and Q queries, each query consists of L and R. Task is to write a program 
which prints the count of numbers which divides all numbers in the given range L-R. 

Link:https://www.geeksforgeeks.org/count-elements-which-divide-all-numbers-in-range-l-r/

We have used segment Tree ,where each node stores count,min and gcd of elements in the given range

"""
from collections import Counter

Arr = [2, 4,6,8,10,12,14,16,18,20] 
INF=1000
S=[(Counter(),INF,0)]*4*len(Arr)  #(counter,min,gcd)

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
    
def build(node,start,end):
    if start==end:
        S[node]=(Counter([Arr[start]]),Arr[start],Arr[start])
        return
    mid=(start+end)//2
    build(2*node+1,start,mid)
    build(2*node+2,mid+1,end)
    S1=S[2*node+1]
    S2=S[2*node+2]
    S[node]=(S1[0]+S2[0],min(S1[1],S2[1]),gcd(S1[2],S2[2]))
    
def query(node,start,end,L,R):
    if R<start or L>end:
        return (Counter(),INF,0)
    if L<=start and end<=R:
        return S[node]
    mid=(start+end)//2
    S1=query(2*node+1,start,mid,L,R)
    S2=query(2*node+2,mid+1,end,L,R)
    return (S1[0]+S2[0],min(S1[1],S2[1]),gcd(S1[2],S2[2]))

build(0,0,len(Arr)-1)
A=query(0,0,len(Arr)-1,0,3)
print("A:{}".format(A))
if A[2]==A[1]:
    print("Ans is {} with count:{}".format(A[2],A[0][A[2]]))
else:
    print("No such number exist")


