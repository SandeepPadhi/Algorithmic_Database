"""
Date:4/03/2021
829. Consecutive Numbers Sum - Leetcode Medium

The following program is solved using concepts of AP
"""

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        
        #Solution 1
        i=1
        cnt=0
        while(i*(i+1)/2 <=N):
            if (N-i*(i-1)/2)%i==0:
                cnt+=1
            
            i+=1
        return cnt
        
        
        #Solution 2
        import math
        n=1
        cnt=0
        while(2*N+n-n**2 >0):
            a=(2*N+n-n**2)/(2*n)
            if math.modf(a)[0]==0:
                cnt+=1
            n+=1
        return cnt
        