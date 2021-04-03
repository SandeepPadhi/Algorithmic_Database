"""
Date:3/04/2021
1029. Two City Scheduling - Leetcode Medium

The following problem is solved using sorting
"""


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key = lambda k : k[0] - k[1])
        n = len(costs) // 2   
        return sum([costs[i][0] + costs[i+n][1] for i in range(n)])