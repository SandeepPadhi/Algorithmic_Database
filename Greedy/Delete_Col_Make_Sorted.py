"""
Date:3/03/2021
944. Delete Columns to Make Sorted - Leetcode Easy

The following program is solved using simple packing and unpacking
"""

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt=0
        for st in zip(*strs):
            prev=-1
            for s in st:
                if ord(s)-97<prev:
                    cnt+=1
                    break
                prev=ord(s)-97
        
        return cnt
        