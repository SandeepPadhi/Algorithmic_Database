"""
Date:16/03/2021
921. Minimum Add to Make Parentheses Valid - Leetcode Medium

The following problem is solved using Stack.
"""
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        Stack=[]
        for s in S:
            if len(Stack)==0:
                Stack.append(s)
            else:
                if s==')' and Stack[-1]=='(':
                    Stack.pop()
                else:
                    Stack.append(s)
        return len(Stack)
        