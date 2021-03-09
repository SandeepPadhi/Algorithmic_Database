"""
Date:6/03/2021

5682. Sum of Beauty of All Substrings - Leetcode Medium

The following program is solved using hashing and storing and using prefix count method
"""
class Solution:
    def beautySum(self, s: str) -> int:
        lookup=[[0]*26]
        for i in range(len(s)):
            if i==0:
                look=[0]*26
                look[ord(s[i])-97]=1
            else:
                look=lookup[-1][:]
                look[ord(s[i])-97]+=1
            lookup.append(look)
        total=0
        MAX=100000
        for i in range(len(lookup)-1):
            for j in range(i+1,len(lookup)):
                minval,maxval=MAX,0
                
                for k in range(26):
                    n=lookup[j][k]-lookup[i][k]
                    if n==0:
                        continue
                    if n>maxval:
                        maxval=n
                    if n<minval:
                        minval=n
                
                total+=(maxval-minval)
                
                    
        
        
        return total

                