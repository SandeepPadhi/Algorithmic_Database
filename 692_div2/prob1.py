"""
Date:19/01/2021
The following program shows TLE
"""

t=int(input())

def find():
    n=int(input())
    b=input()
    result=[0]
    ans=0
    i=0
    for bi in b:
        if result[-1]==int(bi)+1:
            ans+=0
            ans*=10
            result.append(int(bi))
        else:
            ans+=1
            ans*=10
            result.append(int(bi)+1)
    ans/=10

    print(int(ans))

for _ in range(t):
    find()