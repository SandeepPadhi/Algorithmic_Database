"""
Date:23/02/2021
1513. Number of Substrings With Only 1s - Leetcode - Medium

The following problem is solved using two pointer
"""
class Solution:
    def numSub(self, s: str) -> int:
        count=0
        flag=False
        first,last=-1,-1
        M=10**9 + 7
        for i in range(len(s)):
            d=s[i]
            if not flag and d=='1':
                flag=True
                first=i
                last=i
            elif flag and d=='1':
                last=i
            if d=='0' and first!=-1:
                c=(last-first+1)
                count+=(c*(c+1)//2)%M
                flag=False
                last,first=-1,-1
        if first!=-1:
                c=(last-first+1)
                count+=(c*(c+1)//2)%M
        return count%M
            
        