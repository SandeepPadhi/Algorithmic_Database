"""
Date:4/03/2021
38. Count and Say - Leetcode Medium

The following problem is solved using two pointer technique
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        
        def find(S):
            S=[s for s in S]
            left=0
            right=0
            Ans=""
            while(right<len(S)):
                while(right<len(S) and S[left]==S[right]):
                    right+=1
                Ans+=str(right-left)+S[left]
                left=right
            return Ans
                
        i=2
        s='1'
        while(i<=n):
            s=find(s)
            i+=1
        return s
            
            
        
        
        
        