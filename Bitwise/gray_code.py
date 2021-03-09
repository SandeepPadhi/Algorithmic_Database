"""
Date:9/03/2021
89. Gray Code - Leetcode Medium

The following program is solved using bitwise manipulation
"""


class Solution:
    def grayCode(self, n: int) -> List[int]:
        gray=set()
        gray.add(0)
        Ans=[0]
        def find(n,gray,Ans):
            tmp=Ans[-1]
            i=0
            while(i<n):
                if tmp^(1<<i) not in gray:
                    Ans.append(tmp^(1<<i))
                    gray.add(tmp^(1<<i))
                    find(n,gray,Ans)
                    return
                
                i+=1
                
        find(n,gray,Ans)
                    
            
        return Ans
        