"""
Date:22/02/2021
223. Rectangle Area - Leetcode Medium
Important

The following problem is solved using simple maths.
We first check if there are overlaps or not in the rectangle.
"""
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        rect1=(C-A)*(D-B)
        rect2=(G-E)*(H-F)
        inter=0
        X=[(A,1),(C,1),(E,2),(G,2)]
        Y=[(B,1),(D,1),(F,2),(H,2)]
        X.sort()
        Y.sort()
        if X[0][1]==X[1][1] or X[2][1]==X[3][1] or Y[0][1]==Y[1][1] or Y[2][1]==Y[3][1]:
            inter=0
        else:
            inter=(X[2][0]-X[1][0])*(Y[2][0]-Y[1][0])
        return rect1+rect2-inter
    