"""
Date:6/04/2021
149. Max Points on a Line - Leetcode Hard
VERY IMPORTANT
The following program is solved using hashing
"""
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 1
        def solve(x1,y1,x2,y2):
            if x1==x2:
                return math.inf,x1
            m=(y1-y2)/(x1-x2)
            b=y2-m*x2
            return m,b
        
        Line={}
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                x1,y1=points[i][0],points[i][1]
                x2,y2=points[j][0],points[j][1]
                m,b = solve(x1,y1,x2,y2)
                if (m,b) not in Line:
                    Line[(m,b)]=set()
                Line[(m,b)].add(i)
                Line[(m,b)].add(j)
        #print(Line)
        return max(len(Line[(m,b)]) for (m,b) in Line)