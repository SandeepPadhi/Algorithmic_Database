"""
Date:12/02/2021
647. Palindromic Substrings - Medium

The following program is solved using loops..
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s)in (0,1):
            return len(s)
        Ans=0
        for i in range(len(s)):
            #around the center
            l=0
            r=0
            j=i
            #Considering odd palindrome
            while((i-l)>=0 and (i+r)<len(s) and s[i-l]==s[i+r]):
                l+=1
                r+=1
            
            Ans+=l
            l=0
            #Considering even palindrome
            while(((i-1)-l)>=0 and (i+l)<len(s) and s[(i-1)-l]==s[i+l]):
                l+=1
            Ans+=l
        return Ans
            
        
        
        