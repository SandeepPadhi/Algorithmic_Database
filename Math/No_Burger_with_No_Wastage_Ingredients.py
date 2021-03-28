"""
Date:28/03/2021
1276. Number of Burgers with No Waste of Ingredients - Leetcode Medium

The following problem is a maths problem
"""

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        t=tomatoSlices
        c=cheeseSlices
        
        if t&1 or t<c:
            return []
        J=t//2 - c
        S=c -J
        if J<0 or S<0:
            return []
        return [J,S]
        