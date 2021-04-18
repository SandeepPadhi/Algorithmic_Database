"""
Date:18/04/2021
5735. Maximum Ice Cream Bars - Leetcode Medium

The following problem is solved using Sorting
"""
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        S=0
        cnt=0
        for c in costs:
            S+=c
            if S<=coins:
                cnt+=1
            else:
                break
            
            
            
        return cnt
            