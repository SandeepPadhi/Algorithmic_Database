"""
Date:4/01/2021
The following problem is to solve Longest increasing subsequence using BinarySearch+DP 
using O(NlogN)time complexity.
"""
A=[1,3,1,4,5,7,5,1,13]
N=len(A)
INF=10000
D=[INF]*(N+1)
P=[-1]*(N+1)#Stores the ancestors of A[i].It makes use of Ac(Actual Index)
Ac=[-1]*(N+1)#Stores the Array indices of the values stored in D
D[0]=0


def find(i):
    a=A[i]
    l=0
    h=N
    ans=-1
    while(l<=h):
        m=(l+h)//2
        if D[m]<a:
            ans=m
            l=m+1
        else:
            h=m-1
    return ans
    
late=-1
for i in range(N):
    j=find(i)
    D[j+1]=A[i]
    P[i]=Ac[j]
    Ac[j+1]=i
    late=max(late,j+1)

Seq=[]
ind=Ac[late]
while(P[ind]!=-1):
    Seq.append(A[ind])
    ind=P[ind]
Seq.append(A[ind])
Seq.reverse()
print("LIS len:{}".format(late))
print("Longest Increasing Subsequence:{}".format(Seq))


