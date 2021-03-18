"""
Date:18/03/2021
438. Find All Anagrams in a String - leetcode Medium

The following problem is solved using lookup trick of alphabets
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        L=[0]*26
        P=[0]*26
        for c in p:
            P[ord(c)-97]+=1
        for i in range(len(p)):
            c=s[i]
            L[ord(c)-97]+=1
            
        def check():
            if P==L:
                return True
            else:
                return False
                   
        Ans=[]
        left=0
        right=len(p)-1
        while(right<len(s)):
            if check():
                Ans.append(left)
            right+=1
            if right<len(s):
                L[ord(s[right])-97]+=1
            L[ord(s[left])-97]-=1
            left+=1
        return Ans
        
        