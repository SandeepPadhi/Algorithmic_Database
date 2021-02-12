"""
Date:28/01/2021
The following is used to find frequency of element in Range:[L,R]
"""

from bisect import bisect_left,bisect_right,bisect
from collections import defaultdict as dict
Store=dict(list)
S = [2, 8, 6, 9, 8, 6, 8, 2, 11,8,7] 
for i in range(len(S)):
    Store[S[i]].append(i)

def find(E,L,R):
    print(Store[E])
    l=bisect_left(Store[E],L)
    r=bisect_right(Store[E],R)
    print("l:{},r:{}".format(l,r))
    return r-l
print(find(7,1,len(S)-1))

"""
S = [2, 8, 6, 9, 8, 6, 8, 2, 11,8] 
from collections import defaultdict as dict
from bisect import bisect_left,bisect_right,bisect

Store=dict(list)
for i in range(len(S)):
    Store[S[i]].append(i)
    
def find(E,L,R):
    print("find")
    print("L:{},R:{},E:{}".format(L,R,E))
    Arr=Store[E]
    print("Arr:{}".format(Arr))
    ansl=-1
    #leastelement greater than equal E
    l,r=0,len(Arr)-1
    print("first")
    while(l<=r):
        mid=(l+r)//2
        print("l:{} ,mid:{} ,r:{}".format(l,mid,r))

        if Arr[mid]>=L:
            ansl=mid
            r=mid-1
        else:
            l=mid+1
    if ansl==-1:
        return 0
        
    #greatest element less than equal to E
    l,r=0,len(Arr)-1
    ansr=-1
    while(l<=r):
        mid=(l+r)//2
        if Arr[mid]<=R:
            ansr=mid
            l=mid+1
        else:
            r=mid-1
    if ansr==-1:
        return 0
    return ansr-ansl+1
print(find(8,1,6))
    
        


"""