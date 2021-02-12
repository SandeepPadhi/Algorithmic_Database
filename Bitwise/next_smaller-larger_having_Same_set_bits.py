"""
Date:2/01/2021
The following code finds next larger and next smaller number with same number of set bits

VERY IMP:
lINK:https://www.geeksforgeeks.org/closest-next-smaller-greater-numbers-number-set-bits/
"""


n=27
"""
We first store indices of 1's in the number .Then,iterate from from back till zero is found.
"""
def findlarge(n):
    ind=[]
    temp=n
    i=0
    while(temp):
        if temp&1:
            ind.append(i)
        i+=1
        temp>>=1
    ans=0
    i=1
    if len(ind)==1:
        return 1<<(ind[0]+1)
    while(i<len(ind) and ind[i]-ind[i-1]==1):
        i+=1
    i-=1
    ind[i]+=1
    i-=1
    while(i>=0):
        ind[i]=i
        i-=1
    ans=0
    for id in ind:
        ans|=(1<<id)
    return ans    



"""
here,we also we iterate from right to left and find first occurance of 0.
then,we use binary search to find the next greater index with value 1 and then decrement the index by 1

"""
def findsmall(n):
    ind=[]
    temp=n
    i=0
    while(temp):
        if temp&1:
            ind.append(i)
        temp>>=1
        i+=1
    zero=-1
    temp=n
    i=0
    while(temp):
        if temp&1:
            pass
        else:
            zero=i
            break
        temp>>=1
        i+=1
    
    l=0
    h=len(ind)-1
    ansind=-1
    while(l<=h):
        m=(l+h)//2
        if ind[m]>zero:
            ansind=m
            h=m-1
        else:
            l=m+1
    
    ind[ansind]-=1
    j=ind[ansind]-1
    i=ansind-1
    while(i>=0):
        ind[i]=j
        i-=1
        j-=1

    
    
    result=0
    for id in ind:
        result|=(1<<id)
    return result
        

large=findlarge(n)
print("large:{}".format(large))
small=findsmall(n)
print("small:{}".format(small))