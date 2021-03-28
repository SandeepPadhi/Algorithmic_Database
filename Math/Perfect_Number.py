"""
Date:28/03/2021
507. Perfect Number - Leetcode Easy
The following problem is solved using Maths -
"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        S=0
        for n in range(1,int(sqrt(num))+1):
            if n*n>num:
                break
            if num%n==0:
                S+=n
                n2=num//n
                if n2!=n:
                    S+=n2
        S-=num
        if S==num:
            return True
        return False
        