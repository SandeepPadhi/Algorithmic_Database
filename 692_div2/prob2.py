"""
Date:19/1/2021
It seems test cases are incorrent
for d=4,number has to be 20
    d=2,number has to be 12 and not 15
"""

t=int(input())

def find():
    d=int(input())
    d1=1
    d2=1+d
    d3=d2+d
    d41=d2*d3
    d42=(1+d)*4
    print(min(d42,d41))
for _ in range(t):
    find()