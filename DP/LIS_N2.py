"""
Date:4/02/2021
The following problem is to find Longest increasing problem usiing DP in O(N2)
"""
A=[1,3,1,4,5,7,5,10,13]
D=[1]*len(A)
P=[-1]*len(A)
for i in range(1,len(A)):
    for j in range(i-1,-1,-1):
        if A[j]<A[i] and 1+D[j]>D[i]:
            P[i]=j
            D[i]=D[j]+1
ind=D.index(max(D))
print("ind:{}".format(ind))
print("D:{}".format(D))
print("P:{}".format(P))
Seq=[]
while(P[ind]!=-1):
    Seq.append(A[ind])
    ind=P[ind]
Seq.append(A[ind])
Seq.reverse()
print("Seq:{}".format(Seq))

