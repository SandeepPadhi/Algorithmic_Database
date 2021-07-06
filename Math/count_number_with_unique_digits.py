"""
Date:30/06/2021
357. Count Numbers with Unique Digits - Leetcode Medium

Link:https://leetcode.com/problems/count-numbers-with-unique-digits/discuss/83052/Clear-c%2B%2B-explanation-of-combinatorics-using-DP-method

The following problem is solved using combinotorics.
"""

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 10
        dp=[0,10]
        for i in range(2,n+1):
            ans=9
            k=9
            for j in range(1,i):
                ans*=k
                k-=1
            dp.append(ans)
        return sum(dp)

            
            
            
        
        