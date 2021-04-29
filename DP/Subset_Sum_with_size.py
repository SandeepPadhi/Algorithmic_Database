"""
Date:28/04/2021
805. Split Array With Same Average - Leetcode Hard

The following problem is solved using Sets,DP and maths logic.
"""
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n=len(nums)
        total=sum(nums)
        subsize=[set() for _ in range(n+1)]
        subsize[0].add(0)
        Done=True

        #Main logic for subset-sum..it can be easily reused..
        def solve(subsize):
            for a in nums:
                for s in range(n//2,0,-1):
                    for b in subsize[s-1]:
                        subsize[s].add(a+b)
        
        for i in range(1,n//2+1):
            if total*i%n==0:
                if Done:
                    Done=False
                    solve(subsize)
                if (total*i)/n in subsize[i]:
                    return True
        return False
                
    
        
        
        
        
        
        
        
        
        
        
            
            
    