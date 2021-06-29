
"""
Date:20/05/2021
Lexicographic rank of a string - Hard

The program is implementation to find lexicographical Rank
of the given string.

Link:https://www.geeksforgeeks.org/lexicographic-rank-of-a-string/

Time Complexity:O(N)
"""


def fac(N):
    return 1 if N<=1 else N*fac(N-1)

def Count(i,S):
    ans=0
    for j in range(i+1,len(S)):
        if S[j]<S[i]:
            ans+=1
    return ans

def precompute(precom,S):
    for s in S:
        precom[ord(s)]+=1
    for i in range(1,len(precom)):
        precom[i]+=precom[i-1]

def update(precom,s):
    for i in range(ord(s),len(precom)):
        precom[i]-=1

def findLexicographicalRank(S):
    N=len(S)
    mul=fac(len(S))
    rank=0
    precom=[0]*256
    precompute(precom,S)
    
    for i in range(len(S)):#O(N)
        countless=precom[ord(S[i])-1] #0(N)
        mul=mul//(N-i)
        rank = rank + countless*mul#O(N)
        update(precom,S[i])
        
    return rank + 1



S='string'

rank=findLexicographicalRank(S)
print("Rank:{}".format(rank))