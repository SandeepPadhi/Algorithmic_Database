"""
Date:3/04/2021
1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K - Leetcode Medium

The following problem is solved using Binary Search
"""
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        F=[1,1]
        maxval=10**9+7
        while(F[-1]<k):
            F.append(F[-2]+F[-1])
        
        count=0
        while(k>0):
            ind=bisect_left(F,k)
            if ind==len(F):
                ind-=1
            elif F[ind]>k:
                ind-=1
            count+=(k//F[ind])
            k%=F[ind]
            
        
        return count
        