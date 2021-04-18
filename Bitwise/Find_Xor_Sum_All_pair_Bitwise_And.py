"""
Date:18/04/2021
5737. Find XOR Sum of All Pairs Bitwise AND - Leetcode Hard

The following problem is solved using BitWise manipulations
"""
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        
        A1=[0]*32
        A2=[0]*32
        for a in arr1:
            for i in range(32):
                if a&(1<<i):
                    A1[i]+=1
        
        for a in arr2:
            for i in range(32):
                if a&(1<<i):
                    A2[i]+=1
        
        Ans=0
        for i in range(32):
            val=A1[i]*A2[i]
            if val&1:
                Ans+=(1<<i)
        return Ans