"""
Date:13/02/2021
The following program generates all possible combination of a list
"""

A=[1,2,3]
Ans=0
for mask in range(1<<len(A)):
    i=0
    while(mask):
        if mask&1:
            print(A[i],end="")
        mask>>=1
        i+=1
    print()
