"""
Date:4/04/2021

The following program gives smallest prime number of a number.
And if spf of x is x then x is prime number.

Time Complexity:
seive() - O(nloglogn)
getfactorized() - O(logn)
Each query will take O(logn) 

"""

import math

spf=[]#smallest Prime Factor of the number
maxn=100
for i in range(maxn+1):
    spf.append(i)

def seive():
    global spf
        
    for i in range(2,int(math.sqrt(maxn))+1,2):#In seives we only go till sqrt(n),
        #check if its prime number
        if spf[i]==i:
            #Then for all these J's ,i will be the smallest prime factor
            for j in range(i*i,maxn+1,i):
                spf[j]=i

def getfactorized(x,f):
    while(x%f==0):
        x//=f
    return x
seive()
print(spf)
result=[1]
x=32
while(x!=1):
    result.append(spf[x])
    x=getfactorized(x,spf[x])
print(result)
    