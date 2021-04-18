"""
Date:17/04/2021
1735. Count Ways to Make Array With Product - Leetcode Hard

The following program is solved using Maths,Stars and Bars Concept and Prime Factorization
Whenever slots and balls are considered ,solve it using stars and bars
"""
class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        
        mod=10**9 + 7
        
        @lru_cache(None)
        def getPrimeFactor(n):
            F=[]
            i=2
            while(i*i<=n):
                cnt=0
                while(n%i==0):
                    cnt+=1
                    n//=i
                if cnt>0:
                    F.append(cnt)
                i+=1
            if n>1:
                F.append(1)
            return F
        
        Ans=[]
        for n,k in queries:
            ans=1
            for cnt in getPrimeFactor(k):
                ans*=math.comb(cnt+n-1,cnt)
                ans%=mod
            Ans.append(ans)
            
            
        return Ans
            
            
        