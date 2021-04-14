"""
Date:14/04/2021
913. Cat and Mouse - Leetcode Hard

The following problem is solved using min-max+bottom up DP
"""
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        
        @lru_cache(None)
        def dp(m,c,moves):
            if m==c:
                return 2
            if m==0:
                return 1
            if moves>2*len(graph):
                return 0
            
            #mouse's turn
            if moves%2==0:
                draw=False
                for nei in graph[m]:
                    ans=dp(nei,c,moves+1)
                    if ans==1:
                        return 1
                    if ans==0:
                        draw=True
                if draw:
                    return 0
                return 2
            #cat's turn
            else:
                draw=False
                for nei in graph[c]:
                    if nei==0:
                        continue
                    ans=dp(m,nei,moves+1)
                    if ans==2:
                        return 2
                    if ans==0:
                        draw=True
                if draw:
                    return 0
                return 1
        
        
    
        return dp(1,2,0)
        