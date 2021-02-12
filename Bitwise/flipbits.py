"""
Date:28/01/2021
Following problem flips the bits of number.
"""

n=9
np=0
j=0
while(n):
    np+=(1<<j)
    j+=1
    n>>=1
print("np:{}".format(np))
print("Comp:{}".format(np^9))#Final Step of bit flipping

    