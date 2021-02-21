"""
Date:16/02/2021
The following program solves recursively,and finds max number at most k swaps
Link:https://www.geeksforgeeks.org/find-maximum-number-possible-by-doing-at-most-k-swaps/?ref=rp
""" 
A="254"
maxval=A
S=[a for a in A]
k=2
def find(S,index,k):
    global maxval
    if k==0:
        return 
    curchr=S[index]
    maxchr=S[index]
    for i in range(index+1,len(S)):
        if S[i]>maxchr:
            maxchr=S[i]
    if maxchr!=curchr:
        k-=1
    for i in range(index+1,len(S)):
        if S[i]==maxchr:
            S[index],S[i]=S[i],S[index]
            maxval=max(maxval,"".join(S))
            find(S,index+1,k)
            S[index],S[i]=S[i],S[index]

find(S,0,k)
print(maxval)
