"""
Date:5/04/2021
1456. Maximum Number of Vowels in a Substring of Given Length

The following problem is solved using two pointer
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        sub=set()
        left=0
        right=0
        maxlen=0
        count=0
        vowel={'a','e','i','o','u'}
        while(right<k):
            if s[right] in vowel:
                count+=1                
            right+=1
        right-=1
        maxlen=count
        #print("left:{}, right:{} , count:{}".format(left,right,count))
        while(right+1<len(s)):
    
            right+=1
            if s[right] in vowel:
                    count+=1
            if s[left] in vowel:
                        count-=1
            left+=1
            #print("left:{} , right:{} , count:{}".format(left,right,count))
            maxlen=max(maxlen,count)
        return maxlen
            
        
        
            