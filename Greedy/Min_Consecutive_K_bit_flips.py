"""
Date:24/04/2021
995. Minimum Number of K Consecutive Bit Flips - Leetcode Hard

The following problem is solved using Greedy approach.
We learned an important technique called flipping and hit,we keep track of flips.
In addition to this we also use Xor very smartly
"""
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        ans=0
        flip=0
        hint=[0]*len(A)
        N=len(A)
        for i,x in enumerate(A):
            flip^=hint[i]
            if flip^x==0:
                ans+=1
                if i+K>N:
                    return -1
                flip^=1
                if i+K<N:
                    hint[i+K]=1
        return ans
        
        """
        #print("len of A:{}".format(len(A)))
        #return 0
        ans=0
        i=0
        while(i<len(A)-K+1):
            while(i<(len(A)-K+1) and A[i]==1):
                i+=1
            if i<len(A)-K+1:
                ans+=1
                for k in range(i,i+K):
                    A[k]^=1
                i+=1
        if sum(A)==len(A):
            return ans
        return -1

        
        
        """