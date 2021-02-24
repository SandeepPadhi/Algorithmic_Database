
"""
Date:23/02/2021
The following program is solved using gap strategy.
This gap strategy is inspired by Optimal Strategy of Game
Link:https://www.youtube.com/watch?v=ww4V7vRIzSk
"""

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        dp=[[0]*50 for _ in range(50)]
        
        def minpoly(a,b):
            if dp[a][b]!=0 or b-a+1<3 :
                return dp[a][b]
            m=100000000
            for k in range(a+1,b):
                v=A[a]*A[k]*A[b] + minpoly(a,k) +minpoly(k,b)
                m=min(m,v)
            dp[a][b]=m
            return m
        
        minpoly(0,len(A)-1)
        return dp[0][len(A)-1] 
        
        
        
"""


class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
    	SP, LA = [[0]*50 for i in range(50)], len(A)
    	def MinPoly(a,b):
    		L, m = b - a + 1, math.inf; 
    		if SP[a][b] != 0 or L < 3: return SP[a][b]
    		for i in range(a+1,b): m = min(m, A[a]*A[i]*A[b] + MinPoly(a,i) + MinPoly(i,b))
    		SP[a][b] = m; return SP[a][b]
    	return MinPoly(0,LA-1)
		
		
DP - Bottom Up - Without Recursion (Faster): (six lines)

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
    	SP, L = [[0]*50 for _ in range(50)], len(A)
    	for i in range(2,L):
    		for j in range(L-i):
    			s, e, SP[s][e] = j, j + i, math.inf
    			for k in range(s+1,e): SP[s][e] = min(SP[s][e], A[s]*A[k]*A[e] + SP[s][k] + SP[k][e])
    	return SP[0][L-1]
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com



"""