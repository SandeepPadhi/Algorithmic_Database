"""
Date:6/04/2021
446. Arithmetic Slices II - Subsequence - Leetcode Hard

The following problem is solved using Hashing and DP
"""
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        Hash=[dict() for _ in range(len(A))]
        Ans=0 
        for i in range(1,len(A)):
            for j in range(i):
                diff=A[i]-A[j]
                if diff not in Hash[i]:
                    Hash[i][diff]=0
                if diff in Hash[j]:
                    Ans+=Hash[j][diff]
                    Hash[i][diff]+=Hash[j][diff]
                Hash[i][diff]+=1
        return Ans
                    
        