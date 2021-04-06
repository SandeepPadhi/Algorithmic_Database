"""
Date:6/03/2021
474. Ones and Zeroes - Leetcode Medium

The following problem is solved using DP+recursion
"""

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        L=[]
        for s in strs:
            s=[c for c in s]
            #print("s:{}".format(s))
            zero=0
            one=0

            for c in s:
                if c=='0':
                    zero+=1
                else:
                    one+=1
            L.append({"1":one,'0':zero})
        
        @lru_cache(None)
        def find(m,n,ind):#m
            if m<0 or n<0:
                return -10000000
            if ind==-1:
                return 0
            
            maxl=0
            M,N=m-L[ind]['0'],n-L[ind]['1']
            maxl=max(maxl,1+find(M,N,ind-1),find(m,n,ind-1))
            return maxl
        
        maxl=0
        for i in range(len(strs)):
            M,N=m-L[i]['0'],n-L[i]['1']
            maxl=max(maxl,1+find(M,N,i-1),find(m,n,i-1))
        return maxl
            
            
        