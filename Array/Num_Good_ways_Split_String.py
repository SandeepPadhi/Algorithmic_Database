"""
Date:28/02/2021
1525. Number of Good Ways to Split a String - Leetcode Medium

The following program is solved using lists and sets
"""
class Solution:
    def numSplits(self, s: str) -> int:
        leftcount=[1]*len(s)
        rightcount=[1]*len(s)
        leftset=set()
        rightset=set()
        for i in range(len(s)):
            if s[i] not in leftset:
                leftcount[i]+=len(leftset)
                leftset.add(s[i])
            else:
                leftcount[i]=len(leftset)
        for i in range(len(s)-1,-1,-1):
            if s[i] not in rightset:
                rightcount[i]+=len(rightset)
                rightset.add(s[i])
            else:
                rightcount[i]=len(rightset)
        ans=0
        for i in range(len(s)-1):
            if leftcount[i]==rightcount[i+1]:
                ans+=1
        return ans
            
        