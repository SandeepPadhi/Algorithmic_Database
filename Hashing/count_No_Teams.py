"""
Date:24/02/2021
1395. Count Number of Teams - Leetcode - Medium

The following program is using Hashing
"""
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        highindex={}
        lowindex={}
        for i in range(len(rating)):
            highindex[i]=[]
            lowindex[i]=[]
            for j in range(i+1,len(rating)):
                if rating[j]>rating[i]:
                    highindex[i].append(j)
                elif rating[j]<rating[i]:
                    lowindex[i].append(j)
        count=0
        for i in range(len(rating)):
            for j in highindex[i]:
                count+=len(highindex[j])
            for j in lowindex[i]:
                count+=len(lowindex[j])
        return count
    
    
    """
Date:24/02/2021
The following program is solved using simple counting .
"""
    
    """
    def numTeams(self, rating: List[int]) -> int:
        Ans=0
        for i in range(1,len(rating)-1):
            leftlow,lefthigh,rightlow,righthigh=0,0,0,0
            j=i-1
            while(j>=0):
                if rating[j]<rating[i]:
                    leftlow+=1
                elif rating[j]>rating[i]:
                    lefthigh+=1
                j-=1
            j=i+1
            while(j<len(rating)):
                if rating[i]<rating[j]:
                    righthigh+=1
                elif rating[i]>rating[j]:
                    rightlow+=1
                j+=1
            Ans+=(leftlow*righthigh + lefthigh*rightlow)
        return Ans
            
    
    
    
    """