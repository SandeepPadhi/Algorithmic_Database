"""
Date:10/12/2020
The following problem is solved using Max-Min algorithm + DP
Here ,alice tries to maximize the points and Bobs makes his choices such that Alice get minimum possible points

The problem is classical game theory problem
"""
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        M=1
        #Alice=1
        #Bob=-1
        person=1#As Alice starts
        piles=[0]+piles
        for i in range(1,len(piles)):
            piles[i]+=piles[i-1]
        
        
        @lru_cache(None)
        def stone_util(person,start,M):
            if start>=len(piles):
                return 0

            if person==1:
                ans=0
                #max - Alice tries to maximize
                for i in range(1,min(2*M+1,len(piles))):
                    ans_temp=0
                    X=i
                    end=min(start+i-1,len(piles)-1)
                    ans_temp=piles[end]-piles[start-1]
                    ans=max(ans,ans_temp+stone_util(-person,start+i,max(M,X)))
                            
                return ans
            else:
                #Bob tries to Minimize Alices points
                ans=9999999
                for i in range(1,min(2*M+1,len(piles))):
                    X=i        
                    ans=min(ans,stone_util(-person,start+i,max(X,M)))
                return ans
            
            
        ans=stone_util(person,1,1)
        return ans