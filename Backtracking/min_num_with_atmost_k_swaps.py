"""
Date:16/02/2021
The following program solves recursively,and finds min number at most k swaps
Link:https://www.geeksforgeeks.org/find-maximum-number-possible-by-doing-at-most-k-swaps/?ref=rp

"""
A="2544"
minval=A
S=[a for a in A]
k=1
def find(S,index,k):
    global minval
    if k==0 or index>=len(S):
        return
    curchr=S[index]
    minchr=S[index]
    
    for i in range(index,len(S)):
        if S[i]<minchr:
            minchr=S[i]
    if minchr==curchr:
        find(S,index+1,k)
    else:
        for i in range(index+1,len(S)):
            if S[i]==minchr:
                S[index],S[i]=S[i],S[index]
                minval=min(minval,"".join(S))
                find(S,index+1,k-1)
                S[index],S[i]=S[i],S[index]
                
    
find(S,0,k)
print(minval)
