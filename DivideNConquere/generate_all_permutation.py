"""
Date:13/02/2021
The following program generates all possible permutation of a list
"""

A=[1,2,3]
Ans=0
def permutation(A,cid):
    global Ans
    if cid==len(A):
        Ans+=1
        print(A)
        return
    for i in range(cid,len(A)):
        A[i],A[cid]=A[cid],A[i]
        permutation(A,cid+1)
        A[i],A[cid]=A[cid],A[i]
permutation(A,0)
print(Ans)




