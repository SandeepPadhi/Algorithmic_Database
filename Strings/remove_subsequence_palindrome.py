"""
Date:9/03/2021
Remove Palindromic Subsequences- Leetcode Medium
The following program is solved using two pointer
"""
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s)==0:
            return 0
        left,right=0,len(s)-1
        while(left<=right and s[left]==s[right]):
            left+=1
            right-=1
        if left>right:
            return 1
        return 2
        
        
        
        """
        count=0
    
        done=[False]*len(s)
        
        for i in range(len(s)):
            if done[i]:
                continue
            #print("i:{} , done:{}".format(i,done))
            left=i
            right=len(s)-1
            c=0
            while(left<=right):
                while(left<=right and (s[left]!=s[right] or done[right]) ):
                    right-=1
                if left<=right and s[left]==s[right]:
                    #print("left:{},right:{}".format(left,right))
                    done[left],done[right]=True,True
                    c=1
                while(left<right and done[left]):
                    left+=1
            if c==1:
                count+=1
            
                
        
                
        
        
        return min(2,count)
        
        
        
        """