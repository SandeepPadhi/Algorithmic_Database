"""
Date:16/03/2021
119. Pascal's Triangle II - Leetcode Easy

The following problem is solved using simple loops and concept of pascal triangle
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        if rowIndex==2:
            return [1,2,1]
        Prev=[1,2,1]
        Pas=[1,2,1]
        for i in range(3,rowIndex+1):
            Pas=[1]
            for i in range(len(Prev)-1):
                Pas.append(Prev[i]+Prev[i+1])
            Pas.append(1)
            Prev=Pas
        return Pas
        