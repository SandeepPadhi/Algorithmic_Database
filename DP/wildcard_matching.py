"""
Date:20/02/2021
44. Wildcard Matching - Leetcode Medium

The following program is solved using recursion and DP
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def find(i,j):#i==len(s) , j==len(p)
            if i==0 and j==0:
                return True
            if i==0:
                if p[j-1]=='*':
                    return find(i,j-1)
                return False
            if j==0:
                return False
            if s[i-1]==p[j-1] or p[j-1]=='?':
                return find(i-1,j-1)
            elif p[j-1]=='*':
                return find(i-1,j) or find(i,j-1)
            else:
                return False
            
        
        if find(len(s),len(p)):
            return True
        return False
        



"""
class Solution:
    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        if len(s)==0:
            j=0
            while(j<len(p) and p[j]=='*'):
                j+=1
            if j==len(p):
                return True
            return False
        i=0
        while(i<len(p) and i<len(s)):
            if p[i]=='?':
                pass
            elif p[i]=='*':
                j=0
                while(i+j<=len(s)):
                    if self.isMatch(s[i+j:],p[i+1:]):
                        return True
                    j+=1
            else:
                if p[i]!=s[i]:
                    return False
            i+=1
        if i==len(s):
            while(i<len(p)):
                if p[i]!='*':
                    return False
                i+=1
            return True
        return False
                    
        
        
        


"""