"""
Date:7/04/2021
873. Length of Longest Fibonacci Subsequence

The following problem is solved using hashing and loop
"""
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        A={}
        for i in range(len(arr)):
            A[arr[i]]=i
        maxlen=0
        for i in range(2,len(arr)):
            for j in range(1,i):
                l=2
                c,b=arr[i],arr[j]
                d=c-b
                while(d in A and d<b):
                    l+=1
                    c,b=b,d
                    d=c-b
                maxlen=max(maxlen,l)
                
        if maxlen>=3:
            return maxlen
        return 0
                
                    