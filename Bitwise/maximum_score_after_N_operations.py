"""
Date:26/03/2021
1799. Maximize Score After N Operations - Leetcode Hard

The following program is solved using Bitmasking + DP
Space complexity: 0(N*2^N)
Time Complexity: 0(N^2*N*2^N)
"""
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        import math
        N=len(nums)
        gcd=[[1 for _ in range(N)] for _ in range(N)]
        
        for i in range(N):
            for j in range(N):
                gcd[i][j]=math.gcd(nums[i],nums[j])
                
        @lru_cache(None)
        def find(i,mask):
            #print("i:{},mask:{}".format(i,mask))
            if mask==0 or i>N//2:
                return 0
            best=0
            for x in range(N):
                if mask&(1<<x):
                    for y in range(x+1,N):
                        if mask&(1<<y):
                            score = i*gcd[x][y]+ find(i+1,mask^(1<<x)^(1<<y))
                            if score>best:
                                best=score
            return best
        #print("N:{},val:{}".format(N,(1<<N) - 1))    
        return find(1,(1<<N) -1)