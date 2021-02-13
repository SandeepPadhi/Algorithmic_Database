"""
Date:13/02/2021
The following is solved using DP.
Time complexity:O(N)
"""
class Solution:
    def numOfWays(self, n: int) -> int:
        same=[0]*n
        diff=[0]*n
        same[0]=6
        diff[0]=6
        M=10**9 + 7
        
        for i in range(1,n):
            same[i]=same[i-1]*3 + diff[i-1]*2
            diff[i]=same[i-1]*2 + diff[i-1]*2
            
        return (same[-1]+diff[-1])%M
        