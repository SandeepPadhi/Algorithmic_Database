"""
Date:7/04/2021
1227. Airplane Seat Assignment Probability - Leetcode Medium
f(n+1) = 1/(n+1) + (n-1)*f(n)/(n+1) --- where f(n)=1/2
The following problem is solved using probablity and is proved using mathematical induction.
"""
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n^1: # or n>1
            return 0.5
        return 1 #When n==0
