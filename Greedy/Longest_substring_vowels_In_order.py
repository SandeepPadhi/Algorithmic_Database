"""
Date:25/04/2021
1839. Longest Substring Of All Vowels in Order - leetcode medium

The following problem is solved using greedy approach
"""
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        W=[ord(w)-97 for w in word]
        print(W)
        print(len(W))
        #longest increasing substring
        left=0
        right=1
        ans=0
        while(right<len(W)):
            S=set()
            while(right<len(W) and W[right-1]<=W[right]):
                S.add(W[right])
                #ans=max(ans,right-left+1)
                right+=1
            S.add(W[left])
            if len(S)==5:
                ans=max(ans,right-left)
            #print("left:{},right:{},ans:{}".format(left,right,ans))
            left=right
            right+=1
        
        return ans
        