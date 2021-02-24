"""
Date:22/02/2021
1081. Smallest Subsequence of Distinct Characters - Leetcode - Medium

The following problem is solved using greedy+stack
"""
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        lookup=defaultdict(lambda:0)
        for c in s:
            lookup[c]+=1
        Alpha=[False]*26
        Stack=[]
        for c in s:
                
            if not Alpha[ord(c)-97]:
                while(len(Stack)>0 and Stack[-1]>c and lookup[Stack[-1]]>0):
                    Alpha[ord(Stack[-1])-97]=False
                    Stack.pop()

                Stack.append(c)
                Alpha[ord(c)-97]=True
            
            lookup[c]-=1
        return "".join(Stack)
            
        
        