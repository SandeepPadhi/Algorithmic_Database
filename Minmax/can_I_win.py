"""
Date:16/02/2021
464.Can I Win ...Leetcode-Medium
The following program is solved using  Min-Max algorithm
"""
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        maxc=maxChoosableInteger
        if maxc*(maxc+1)//2 < desiredTotal:
            return False
        M=[i for i in range(1,maxChoosableInteger+1)]
        @lru_cache(None)
        def find(M,desiredTotal,Player):
            if desiredTotal<=0:
                return True if Player==1 else False
            if Player==0:
                for i,e in enumerate(M):
                    if  find(tuple(M[:i]+M[i+1:]),desiredTotal-e,1):
                        return True
                return False
            else:
                for i,e in enumerate(M):
                    if not find(tuple(M[:i]+M[i+1:]),desiredTotal-e,0):
                        return False
                return True

                
                    
                        
        
        if desiredTotal<=0:
            return True
        
        return find(tuple(M),desiredTotal,0)    
        
        """
        choose=[i for i in range(1,maxChoosableInteger+1)]
        Player=1#1-player1,  -1 - player2
        total=0
        M=maxChoosableInteger
        if M*(M+1)//2 < desiredTotal:
            return False
        
        while(True):
            if Player==1:
                if choose[-1]>=desiredTotal:
                    return True
                desiredTotal-=choose[0]
                choose.pop(0)
            else:
                if choose[-1]>=desiredTotal:
                    return False
                desiredTotal-=choose[0]
                choose.pop(0)
            
            Player=-Player
        
        
        
        """
            
        
        