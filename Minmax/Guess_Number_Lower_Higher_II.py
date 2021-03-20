"""
Date:18/03/2021
375. Guess Number Higher or Lower II

The following is solved by Min-Max Algorithm
"""
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        @lru_cache(None)
        def find(start,end):
            if start>=end:
                return 0
            Ans = 10000000
            for i in range(start,end+1):
                Ans = min(Ans,i+ max(find(start,i-1),find(i+1,end)))
            return Ans
                
            
            
        Ans = find(1,n)
        
        
        
        
        return Ans
            