"""
Date:16/04/2021
421. Maximum XOR of Two Numbers in an Array - Leetcode Medium

The following program is solved using Trie--Implemented using dictionary(MAP)
"""
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root={}
        
        def insert(num):
            nonlocal root
            curr=root
            for i in range(31,-1,-1):
                bit=(num>>i)&1
                if bit not in curr:
                    curr[bit]={}
                curr=curr[bit]
            curr['#']=num
        
        def query(num):
            nonlocal root
            curr=root
            for i in range(31,-1,-1):
                target = ((num>>i)&1)^1
                if target in curr:
                    curr=curr[target]
                else:
                    curr=curr[target^1]
            return num^curr['#']
        
        for num in nums:
            insert(num)
        
        Ans=0
        for num in nums:
            Ans=max(Ans,query(num))
        return Ans