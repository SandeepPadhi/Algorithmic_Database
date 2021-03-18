"""
Date:18/03/2021
1052. Grumpy Bookstore Owner - Leetcode Medium

The following problem is solved using Sliding Window
"""

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        Total=sum(customers)
        N=len(customers)
        G=[]
        for i in range(len(grumpy)):
            if grumpy[i]==1:
                Total-=customers[i]
                G.append(i)
        
        Best=Total
        left=0
        right=0
        val=0
        
        while(left<=right and right<len(G)):
            while(left<=right and G[right]-G[left]>=X ):
                Best=max(Best,Total+val)
                val-=customers[G[left]]
                left+=1
            if left>right:
                left=right
            val+=customers[G[right]]
            right+=1
        right-=1
        
        while(left<=right and G[right]-G[left]>=X ):
                Best=max(Best,Total+val)
                val-=customers[G[left]]
                left+=1
        
        return max(Best,Total+val)
            
        
                    
            
        
        
        