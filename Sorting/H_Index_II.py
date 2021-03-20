"""
Date:18/03/2021
275. H-Index II

The following problem is solved using sorting
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.reverse()
        citations+=[-1]
        
        H=0
        for i in range(len(citations)-1):
            if citations[i]>=i+1 and citations[i+1]<=i+1:
                H=max(H,i+1)
        return H
        