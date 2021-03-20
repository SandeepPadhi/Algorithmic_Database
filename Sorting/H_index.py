"""
Date:18/03/2021
274. H-Index

The following problem is solved using Sorting
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        citations+=[-1]
        print("citations:{}".format(citations))
        H=0
        for i in range(len(citations)-1):
            if citations[i]>=i+1 and citations[i+1]<=i+1:
                H=max(H,i+1)
        return H
        
        
        