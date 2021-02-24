"""
Date:23/02/2021
6. ZigZag Conversion - Leetcode Medium

The following program is solved using simple loop logic
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i=0
        L=[[] for _ in range(numRows)]
        dir=True
        for c in s:
            L[i%numRows].append(c)
            if i==0:
                dir=True
                i+=1
            elif i==numRows-1:
                dir=False
                i-=1
            else:
                if dir:
                    i+=1
                else:
                    i-=1
           
            
           
        Ans=""
        for l in L:
            Ans+="".join(l)
        return Ans
            
            
                
        