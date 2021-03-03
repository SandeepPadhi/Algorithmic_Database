def find():
    n,m=map(int,input().split())
    A=map(int,input().split())
    B=map(int,input().split())
    
    l,r=0,len(A)
    Af=0
    while(l<=r):
        m=(l+r)//2
        if A[m]>=0:
            Af=m
            r=m-1
        else:
            l=m+1
    
    l,r=0,len(B)
    Bf=0
    while(l<=r):
        m=(l+r)//2
        if B[m]>=0:
            Bf=m
            r=m-1
        else:
            l=m+1
    
    Ar,Br,Al,Bl=A[Af:],B[Bf:],A[:Af],B[:Bf]
    

t=int(input())
for _ in range(t):
    find()
