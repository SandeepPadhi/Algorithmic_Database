"""
Date:25/03/2021
3.Max_pre - Hackerrank - College contest

The following problem is solved using Sorting + Greedy approach

"""


n=int(input())
C=list(map(int,input().split()))
C.sort()
prev=0
for c in C:
    if prev+1>=c:
        prev+=c
    else:
        break
print(prev+1) 