"""
Date:16/02/2021
486.Predict The Winner - Leetcode
The following program is solved using min-max algorithm
"""

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        Total=sum(nums)
        
        @lru_cache(None)
        def game(num,s1,s2,Player):
            if len(num)==0:
                if s1>=s2:
                    return True
                return False
                
            if Player==0:
                if game(tuple(num[1:]),s1+num[0],s2,1):
                    return True
                if game(tuple(num[:len(num)-1]),s1+num[-1],s2,1):
                    return True
                return False
            else:
                if not game(tuple(num[1:]),s1,num[0]+s2,0):
                    return False
                if not game(tuple(num[:len(num)-1]),s1,num[-1]+s2,0):
                    return False
                return True
        
        return game(tuple(nums),0,0,0)