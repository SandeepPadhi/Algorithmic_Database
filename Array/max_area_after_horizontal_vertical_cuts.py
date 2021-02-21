"""
Date:21/02/2021
1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts - Leetcode Medium
The following problem is simple sorting problem for find the max area.
"""
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        last=0
        maxhor=0
        M=10**9 + 7
        for hor in horizontalCuts:
            maxhor=max(maxhor,hor-last)
            last=hor
        maxhor=max(maxhor,h-horizontalCuts[-1])
        
        verticalCuts.sort()
        last=0
        maxver=0
        for wid in verticalCuts:
            maxver=max(maxver,wid-last)
            last=wid
        maxver=max(maxver,w-verticalCuts[-1])
        
        return maxver*maxhor%M