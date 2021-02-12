"""
Date:28/01/2021
Following program prints all possible combinations using bitwise manipulations
"""


S=[1,3,4,5,6,7]
N=len(S)
Target=7
for mask in range(1<<N):
    j=0
    E=[]
    Sum=0
    while(mask):
        if mask&1:
            Sum+=S[j]
            E.append(S[j])
        j+=1
        mask>>=1
    print("Element:{}".format(E))
    
        
            