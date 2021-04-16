"""
Date:15/04/2021
1467. Probability of a Two Boxes Having The Same Number of Distinct Balls - Leetcode Hard

The following problem is solved using probablity and combinatorics
"""
class Solution:
    def getProbability(self, balls: List[int]) -> float:
        
        M=len(balls)
        N=sum(balls)
        
                
        Total=math.factorial(N)//math.prod(math.factorial(n) for n in balls)
        valid=0
        s1=[0]*M
        s2=[0]*M
        
        def find(ind):
            nonlocal s1,s2,valid
            if ind==M:
                if sum(s1)==sum(s2) and len([n for n in s1 if n])==len([n for n in s2 if n]):
                    base1=math.factorial(sum(s1))//math.prod(math.factorial(n) for n in [s for s in s1 if s])
                    base2=math.factorial(sum(s2))//math.prod(math.factorial(n) for n in [s for s in s2 if s])
                    valid+=base1*base2
                return
            
            for k in range(balls[ind]+1):
                s1[ind]=k
                s2[ind]=balls[ind]-k
                find(ind+1)
            
        
        find(0)
        return valid/Total