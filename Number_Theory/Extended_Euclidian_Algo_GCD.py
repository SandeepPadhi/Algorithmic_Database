"""
Date:23/02/2021
The following program is implementation of Extended Euclidian Algo for GCD.
We find coefficient x and y for ax + by=gcd(a,b)
"""
def gcd(a,b):
    if b==0:
        return a,1,0
    g,x1,y1=gcd(b,a%b)
    y=x1-(a//b)*y1
    x=y1
    return g,x,y
print(gcd(14,24))