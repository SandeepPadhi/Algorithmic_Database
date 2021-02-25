"""
Date:25/02/2021
1347. Minimum Number of Steps to Make Two Strings Anagram - Leetcode - Medium

The following program is solved using counting technique.
"""

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count1=[0]*26
        count2=[0]*26
        for w in s:
            count1[ord(w)-97]+=1
        for w in t:
            count2[ord(w)-97]+=1
            
        for i in range(26):
            if count1[i]!=0 and count2[i]!=0:
                if count1[i]>=count2[i]:
                    count1[i]-=count2[i]
                    count2[i]=0
                else:
                    count2[i]-=count1[i]
                    count1[i]=0
       
        return sum(count1)
        
        