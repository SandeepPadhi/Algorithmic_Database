"""
Date:3/04/2021
526. Beautiful Arrangement - Leetcode Medium

The following problem is solved using making all possible permuations
"""
class Solution:
    def countArrangement(self, n: int) -> int:
        
        A=[i+1 for i in range(n)]
        count=0
        def perm(A,ind):
            nonlocal count
            if ind==n:
                for i in range(n):
                    if A[i]%(i+1)==0 or (i+1)%A[i]==0:
                        pass
                    else:
                        return
                count+=1
                return 
            for i in range(ind,n):
                if A[i]%(ind+1)==0 or (ind+1)%A[i]==0:
                    A[ind],A[i]=A[i],A[ind]
                    perm(A,ind+1)
                    A[ind],A[i]=A[i],A[ind]
        perm(A,0)
        return count
            
        