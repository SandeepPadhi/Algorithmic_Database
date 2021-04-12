"""
Date:7/04/2021
1478. Allocate Mailboxes - Leetcode Hard

Ref link:https://www.youtube.com/watch?v=ECcJUqdumIo

One important observation is that if we have to minimize distance cost between interval,always
place the mailbox(it can be anyother thing) , at the middle house(it can be anyother thing).

This pattern is repeated in many places.

The following program is solved using DP
"""

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        cost=[[0 for _ in range(101)] for _ in range(101)]
        for i in range(len(houses)):
            for j in range(i,len(houses)):
                for x in range(i,j+1):
                    cost[i][j]+=abs(houses[(i+j)//2] - houses[x])
        
        dp=[[-1 for _ in range(101)] for _ in range(101)]
        
        def find(dp,start,k):
            if k==0 and start==len(houses):
                return 0
            if k==0 or start==len(houses):
                return math.inf
            if dp[start][k]!=-1:
                return dp[start][k]
            mincost=math.inf
            for x in range(start,len(houses)):
                mincost=min(mincost,cost[start][x]+find(dp,x+1,k-1))
            dp[start][k]=mincost
            return mincost
        
        return find(dp,0,k)