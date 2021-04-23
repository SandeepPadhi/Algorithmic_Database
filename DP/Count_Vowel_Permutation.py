"""
Date:22/04/2021
1220. Count Vowels Permutation - Leetcode Hard

The following problem is solved DP
"""
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        Ans=0
        mod=10**9 + 7
        @lru_cache(None)
        def find(last,n):
            Ans=0
            if n==0:
                return 1
            if last=='a':
                Ans+=find('e',n-1)
            elif last=='e':
                Ans+=find('a',n-1)
                Ans+=find('i',n-1)
            elif last=='i':
                Ans+=find('a',n-1)
                Ans+=find('e',n-1)
                Ans+=find('o',n-1)
                Ans+=find('u',n-1)
            elif last=='o':
                Ans+=find('i',n-1)
                Ans+=find('u',n-1)
            else:
                Ans+=find('a',n-1)
            Ans%=(10**9 + 7)
            return Ans
            
            
            
        #a
        Ans+=find('a',n-1)
        Ans%=mod
        #e
        Ans+=find('e',n-1)
        Ans%=mod
        #i
        Ans+=find('i',n-1)
        Ans%=mod
        #o
        Ans+=find('o',n-1)
        Ans%=mod
        #u
        Ans+=find('u',n-1)
        Ans%=mod
        
        
        return Ans
        