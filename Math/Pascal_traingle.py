"""
Date:16/03/2021
118. Pascal's Triangle - Leetcode Easy

The following problem is simple Pascal Triangle problem
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        Pas=[[1]]
        for i in range(1,numRows):
            Ans=[1]
            for i in range(len(Pas[-1])-1):
                Ans.append(Pas[-1][i]+Pas[-1][i+1])
            Ans.append(1)
            Pas.append(Ans)
        return Pas
        