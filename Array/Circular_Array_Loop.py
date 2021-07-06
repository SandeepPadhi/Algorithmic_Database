"""
Date:30/06/2021
457. Circular Array Loop - Leetcode Medium

The following problem is solved using Two pointer and logic
"""

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        N=len(nums)
        Done=[0]*N
        for pt in range(N):
            if Done[pt]==0:
                Done[pt]=pt+N
                sign=-1
                if nums[pt]>0:
                    sign=1
                ind=(pt+nums[pt])%N
        
                k=1
                indprev=pt
                while(Done[ind]!=(pt+N) and nums[ind]*sign>0):
                    Done[ind]=(pt+N)
                    indprev=ind
                    ind=ind+nums[ind]
                    ind%=N
                    k+=1

                if (ind==pt or Done[ind]==(pt+N)) and k>1 and indprev!=ind:
                    return True
        
        
        return False
