"""
Date:17/04/2021
956. Tallest Billboard - Leetcode Hard

The following problem is solved using DP.
Important thing to note here is that whenever left bucket and right bucket types questions are encountered,use DP(diff,ind)
"""
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        @lru_cache(None)
        def dp(diff,ind):
            if ind==len(rods):
                if diff==0:
                    return 0
                return -10000000000
            
            return max(rods[ind] + max(dp(diff-rods[ind],ind+1),dp(diff+rods[ind],ind+1)),dp(diff,ind+1))
        return dp(0,0)//2
        
        
        
        
        #[1,2,4,8,16,32,64,128,256,512,50,50,50,150,150,150,100,100,100,123]
        