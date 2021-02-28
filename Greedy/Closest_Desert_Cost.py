"""
Date:28/02/2021
1774. Closest Dessert Cost - Leetcode Medium
The following program is solved using brute-force recursion
"""
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        best=10**8
        def find(cost,topind):
            nonlocal best
            if topind==len(toppingCosts):
                if abs(target-best)>abs(target-cost):
                    best=cost
                if abs(target-best)==abs(target-cost) and cost<best:
                    best=cost
                return
            find(cost,topind+1)
            find(cost+toppingCosts[topind],topind+1)
            find(cost+2*toppingCosts[topind],topind+1)

        for b in baseCosts:
            find(b,0)
        return best
        
        