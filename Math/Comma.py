"""
Date:26/03/2021

The following problem is solved using Math
"""


T=int(input())

def find():
    import math
    N=int(input())
    count=0
    X=1000
    mod = 10**9+7
    while(X<=N):
        count+=(N-X+1)
        X*=1000
    print(count)
    
        
    

for _ in range(T):
    find()