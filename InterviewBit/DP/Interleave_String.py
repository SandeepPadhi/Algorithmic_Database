"""
Date:27/05/2021

"""

from functools import lru_cache
class Solution:
	# @param A : string
	# @param B : string
	# @param C : string
	# @return an integer
	def isInterleave(self, A, B, C):
	    
        lena=len(A)
	    lenb=len(B)
	    lenc=len(C)
	    #dp[lena][lenb][lenc]
	    dp=[[[False]*(lenc+1) for _ in range(lenb+1)] for _ in range(lena+1)]
	    dp[0][0][0]=True
	    for i in range(lena+1):
	        for j in range(lenb+1):
	            dp[i][j][0]=True
	   
        for k in range(lenc+1):
            for i in range(lena+1):
                for j in range(lenb+1):
                    #if i==1 and j==0 and k==1:
                    #    print("YES")
                    m=1
                    while(i-m>=0 and k-m>=0 and A[i-m]==C[k-m] and not dp[i][j][k]):
                        dp[i][j][k]|=dp[i-m][j][k-m]
                        m+=1
                    
                    m=1
                    while(j-m>=0 and k-m>=0 and B[j-m]==C[k-m] and not dp[i][j][k]):
                        dp[i][j][k]|=dp[i][j-m][k-m]
                        m+=1
                        
                    
	                                    
	    #print(dp[1][0][1])
	    #print(dp)
	    return 1 if dp[-1][-1][-1] else 0     
	                   
	               
	                    
	    
	    
	        

