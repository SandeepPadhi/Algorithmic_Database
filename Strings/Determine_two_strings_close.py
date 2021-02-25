"""
Date:25/02/2021

1657. Determine if Two Strings Are Close - Leetcode Medium

The following program is solved using hashing and sorting technique.
Basis idea behind is that both words must have same characters and the counts of those characters in word1 must be
same as iin another word,order doesnt matter..just counts are what is required..because numbers can be swapped and
channged...basic idea then is to sort and use hashing techniques
"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        #solution1
        if set(w for w in word1)!=set(w for w in word2):
            return False
        count1=[0]*26
        count2=[0]*26
        for w in word1:
            count1[ord(w)-97]+=1
        for w in word2:
            count2[ord(w)-97]+=1
        count1.sort()
        count2.sort()
        for i in range(26):
            if count1[i]!=count2[i]:
                return False
        return True
    
      
        #solution2
        """

        #word1=[w for w in word1]
        #word2=[w for w in word2]
        if set(word1)!=set(word2) or len(word1)!=len(word2):
            return False
        lookup1={}
        lookup2={}
        for i in range(len(word1)):
            if word1[i] not in lookup1:
                lookup1[word1[i]]=0
            lookup1[word1[i]]+=1
            
        for i in range(len(word1)):
            if word2[i] not in lookup2:
                lookup2[word2[i]]=0
            lookup2[word2[i]]+=1
        
        count1 = sorted(lookup1.values())
        count2 = sorted(lookup2.values())
        
        if count1==count2:
            return True
        return False
            
        

"""
        
        
            
        