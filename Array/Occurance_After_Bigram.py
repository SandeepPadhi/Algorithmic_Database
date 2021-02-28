"""
Date:25/02/2021
1078. Occurrences After Bigram - Leetcode Easy

The following problems are solved using simple loop and comparision
"""

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        Ans=[]
        text=[t for t in text.split(" ")]
        i=0
        while(i+2<len(text)):
            while(i+2<len(text) and not (text[i]==first and text[i+1]==second)):
                i+=1
            if i+2<len(text):
                Ans.append(text[i+2])
            i+=1
        return Ans
        